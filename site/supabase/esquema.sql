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
  -- celular com DDI e DDD, só dígitos (ex.: 5521999998888), pronto para o WhatsApp
  telefone text,
  tipo text not null default 'aluno' check (tipo in ('aluno', 'professor', 'admin')),
  -- nível de ensino do aluno (desde 22/10/2026): fundamental1 (1º a 5º ano),
  -- fundamental2 (6º a 9º ano), medio (1º a 3º ano) ou graduacao (1º a 5º período).
  -- O aluno vê só as disciplinas do seu nível. Só o administrador muda.
  nivel text check (nivel in ('fundamental1', 'fundamental2', 'medio', 'graduacao')),
  -- curso do aluno da Graduação (desde 23/10/2026), ex.: 'sistemas-para-internet'. Vazio
  -- nos outros níveis. Só o administrador muda.
  curso text,
  -- ano ou período dentro do nível, informado no cadastro: o aluno vê as disciplinas do
  -- seu ano/período e dos anteriores. Só o administrador muda.
  periodo smallint check (periodo between 1 and 9),
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
alter table public.perfis add column if not exists telefone text;

-- Níveis de ensino (22/10/2026). As contas que já existiam são todas da Graduação. O
-- período passa a ir até 9 (o Fundamental II usa do 6º ao 9º ano), e cada nível só aceita
-- os seus anos/períodos.
alter table public.perfis add column if not exists nivel text
  check (nivel in ('fundamental1', 'fundamental2', 'medio', 'graduacao'));
update public.perfis set nivel = 'graduacao' where nivel is null and tipo = 'aluno';
alter table public.perfis drop constraint if exists perfis_periodo_check;
alter table public.perfis add constraint perfis_periodo_check check (periodo between 1 and 9);
alter table public.perfis drop constraint if exists perfis_nivel_periodo_check;
alter table public.perfis add constraint perfis_nivel_periodo_check check (
  periodo is null or nivel is null
  or (nivel = 'fundamental1' and periodo between 1 and 5)
  or (nivel = 'fundamental2' and periodo between 6 and 9)
  or (nivel = 'medio' and periodo between 1 and 3)
  or (nivel = 'graduacao' and periodo between 1 and 5)
);

-- Cursos da Graduação (23/10/2026). Os alunos da Graduação que já existiam são todos de
-- Sistemas para Internet. Só a Graduação tem curso.
alter table public.perfis add column if not exists curso text;
update public.perfis set curso = 'sistemas-para-internet'
  where curso is null and tipo = 'aluno' and nivel = 'graduacao';
alter table public.perfis drop constraint if exists perfis_curso_check;
alter table public.perfis add constraint perfis_curso_check check (
  curso is null or (nivel = 'graduacao' and curso ~ '^[a-z0-9-]{1,60}$')
);

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
    if new.nivel is distinct from old.nivel then
      raise exception 'Só um administrador pode mudar o nível de ensino.';
    end if;
    if new.curso is distinct from old.curso then
      raise exception 'Só um administrador pode mudar o curso.';
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
-- Pela aba "Sou aluno": com o nome, o nível, o curso (só na Graduação; sem curso válido,
-- Sistemas para Internet), o ano/período e, se informados, a matrícula e o
-- telefone (opcionais desde 22/10/2026). Sem nível válido, o aluno fica na Graduação; um
-- ano/período que não existe no nível fica vazio (a administração corrige).
-- Pela aba "Sou professor": com o nome e, se informado, o telefone; o pedido fica em análise.
-- Ninguém se cadastra como administrador: o administrador muda o perfil depois.
create or replace function public.criar_perfil()
returns trigger
language plpgsql
security definer
set search_path = public
as $$
declare
  professor boolean := coalesce((new.raw_user_meta_data ->> 'professor') = 'true', false);
  v_nivel text;
  v_curso text;
  v_periodo smallint;
begin
  if not professor then
    v_nivel := case when (new.raw_user_meta_data ->> 'nivel') in ('fundamental1', 'fundamental2', 'medio', 'graduacao')
                    then new.raw_user_meta_data ->> 'nivel' else 'graduacao' end;
    if v_nivel = 'graduacao' then
      v_curso := case when (new.raw_user_meta_data ->> 'curso') ~ '^[a-z0-9-]{1,60}$'
                      then new.raw_user_meta_data ->> 'curso' else 'sistemas-para-internet' end;
    end if;
    if (new.raw_user_meta_data ->> 'periodo') ~ '^[1-9]$' then
      v_periodo := (new.raw_user_meta_data ->> 'periodo')::smallint;
      if not ((v_nivel = 'fundamental1' and v_periodo between 1 and 5)
           or (v_nivel = 'fundamental2' and v_periodo between 6 and 9)
           or (v_nivel = 'medio' and v_periodo between 1 and 3)
           or (v_nivel = 'graduacao' and v_periodo between 1 and 5)) then
        v_periodo := null;
      end if;
    end if;
  end if;

  insert into public.perfis (id, nome, matricula, email, telefone, nivel, curso, periodo, solicita_professor, aceite_privacidade_em)
  values (
    new.id,
    coalesce(nullif(new.raw_user_meta_data ->> 'nome', ''), split_part(new.email, '@', 1)),
    case when professor then null else nullif(trim(new.raw_user_meta_data ->> 'matricula'), '') end,
    new.email,
    nullif(regexp_replace(coalesce(new.raw_user_meta_data ->> 'telefone', ''), '\D', '', 'g'), ''),
    v_nivel,
    v_curso,
    v_periodo,
    professor,
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

-- Avisa a API do Supabase que o esquema mudou (colunas novas passam a valer na hora).
notify pgrst, 'reload schema';
