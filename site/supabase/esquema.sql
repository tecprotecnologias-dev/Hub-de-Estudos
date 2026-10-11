-- ============================================================================
-- Hub de Estudos: cadastro, perfis e regras de acesso (Supabase / PostgreSQL)
--
-- Como usar: no painel do Supabase, abra SQL Editor, cole este arquivo inteiro e
-- clique em Run. Pode rodar de novo sem problema (os comandos substituem o que já
-- existe).
--
-- Depois de criar a SUA conta no site (pela aba "Sou professor"), torne-se
-- administradora rodando:
--   update public.perfis set tipo = 'admin', solicita_professor = false
--   where email = 'seu-email@exemplo.com';
-- ============================================================================

-- Perfil de cada pessoa cadastrada (o login, a senha e o e-mail ficam em auth.users,
-- tabela do próprio Supabase; aqui ficam só os dados do site).
create table if not exists public.perfis (
  id uuid primary key references auth.users (id) on delete cascade,
  nome text not null,
  -- matrícula na instituição: única (uma conta por matrícula); só o administrador muda
  matricula text unique,
  email text not null,
  tipo text not null default 'aluno' check (tipo in ('aluno', 'professor', 'admin')),
  -- período do curso (1 a 5) informado no cadastro: o aluno vê as disciplinas do seu
  -- período e dos anteriores (as optativas, para todos). Só o administrador muda.
  periodo smallint check (periodo between 1 and 5),
  -- cadastro feito pela aba "Sou professor": fica em análise (sem acesso ao conteúdo)
  -- até o administrador aprovar, quando o tipo passa a professor
  solicita_professor boolean not null default false,
  aceite_privacidade_em timestamptz,
  criado_em timestamptz not null default now()
);

-- para quem já tinha criado a tabela antes da coluna de período existir
alter table public.perfis add column if not exists periodo smallint check (periodo between 1 and 5);
alter table public.perfis add column if not exists matricula text unique;
alter table public.perfis add column if not exists solicita_professor boolean not null default false;

alter table public.perfis enable row level security;

-- Quem está logado pode consultar e editar a tabela, mas só dentro das regras (RLS)
-- abaixo. Quem não está logado (anon) não tem acesso nenhum. Necessário nos projetos em
-- que o Supabase não libera tabelas novas automaticamente.
grant select, update on public.perfis to authenticated;
revoke all on public.perfis from anon;

-- O usuário logado é administrador? (security definer: consulta a tabela sem
-- passar pelas regras abaixo, para não entrar em laço)
create or replace function public.eh_admin()
returns boolean
language sql
stable
security definer
set search_path = public
as $$
  select exists (select 1 from public.perfis where id = auth.uid() and tipo = 'admin');
$$;

-- Regras de acesso (RLS): cada pessoa lê e edita só o próprio perfil;
-- o administrador lê e edita todos. Ninguém apaga perfis por aqui.
drop policy if exists "ler o próprio perfil" on public.perfis;
create policy "ler o próprio perfil" on public.perfis
  for select using (id = auth.uid());

drop policy if exists "administrador lê todos" on public.perfis;
create policy "administrador lê todos" on public.perfis
  for select using (public.eh_admin());

drop policy if exists "editar o próprio perfil" on public.perfis;
create policy "editar o próprio perfil" on public.perfis
  for update using (id = auth.uid()) with check (id = auth.uid());

drop policy if exists "administrador edita todos" on public.perfis;
create policy "administrador edita todos" on public.perfis
  for update using (public.eh_admin());

-- Ninguém muda o próprio tipo (aluno -> admin, por exemplo), o período, a matrícula nem
-- o e-mail:
-- só um administrador. Pelo SQL Editor do painel (sem usuário logado) também pode.
create or replace function public.proteger_perfil()
returns trigger
language plpgsql
security definer
set search_path = public
as $$
begin
  if auth.uid() is not null and not public.eh_admin() then
    if new.tipo is distinct from old.tipo then
      raise exception 'Só um administrador pode mudar o perfil de acesso.';
    end if;
    if new.periodo is distinct from old.periodo then
      raise exception 'Só um administrador pode mudar o período.';
    end if;
    if new.matricula is distinct from old.matricula then
      raise exception 'Só um administrador pode mudar a matrícula.';
    end if;
    if new.solicita_professor is distinct from old.solicita_professor then
      raise exception 'Só um administrador pode aprovar o cadastro de professor.';
    end if;
    new.email := old.email;
    new.criado_em := old.criado_em;
  end if;
  return new;
end;
$$;

drop trigger if exists proteger_perfil on public.perfis;
create trigger proteger_perfil
  before update on public.perfis
  for each row execute function public.proteger_perfil();

-- Quando alguém se cadastra, o perfil é criado automaticamente, sempre como aluno.
-- Pela aba "Sou aluno": com o nome, a matrícula e o período do formulário.
-- Pela aba "Sou professor": só com o nome, e o pedido de professor fica em análise.
-- Ninguém se cadastra como administrador: o administrador muda o perfil depois.
create or replace function public.criar_perfil()
returns trigger
language plpgsql
security definer
set search_path = public
as $$
begin
  insert into public.perfis (id, nome, matricula, email, periodo, solicita_professor, aceite_privacidade_em)
  values (
    new.id,
    coalesce(nullif(new.raw_user_meta_data ->> 'nome', ''), split_part(new.email, '@', 1)),
    case when (new.raw_user_meta_data ->> 'professor') = 'true' then null
         else nullif(trim(new.raw_user_meta_data ->> 'matricula'), '') end,
    new.email,
    case when (new.raw_user_meta_data ->> 'professor') = 'true' then null
         when (new.raw_user_meta_data ->> 'periodo') in ('1', '2', '3', '4', '5')
         then (new.raw_user_meta_data ->> 'periodo')::smallint end,
    coalesce((new.raw_user_meta_data ->> 'professor') = 'true', false),
    case when (new.raw_user_meta_data ->> 'aceite_privacidade') = 'true' then now() end
  )
  on conflict (id) do nothing;
  return new;
end;
$$;

drop trigger if exists ao_cadastrar on auth.users;
create trigger ao_cadastrar
  after insert on auth.users
  for each row execute function public.criar_perfil();

-- Excluir a própria conta (direito previsto na LGPD): apaga o login e, em cascata,
-- o perfil. Só funciona para o próprio usuário logado.
create or replace function public.excluir_minha_conta()
returns void
language sql
security definer
set search_path = public
as $$
  delete from auth.users where id = auth.uid();
$$;

revoke all on function public.excluir_minha_conta() from public, anon;
grant execute on function public.excluir_minha_conta() to authenticated;

-- A matrícula já está cadastrada? Usada pela tela de cadastro antes de criar a conta, para
-- avisar o aluno. Responde só verdadeiro ou falso, sem mostrar dados de ninguém.
create or replace function public.matricula_em_uso(m text)
returns boolean
language sql
stable
security definer
set search_path = public
as $$
  select exists (select 1 from public.perfis where matricula = trim(m));
$$;

grant execute on function public.matricula_em_uso(text) to anon, authenticated;
