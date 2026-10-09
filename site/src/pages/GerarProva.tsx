import { useEffect, useState } from 'react'
import { questoes } from '../data/questoes'
import { NOMES_NIVEL, type Questao } from '../data/tipos'
import Filtros from '../lib/Filtros'
import { embaralhar, embaralharAlternativas, filtrar, FILTRO_VAZIO, LETRAS, nomeDisciplina, type Filtro } from '../lib/util'
import { apostilas } from '../data/apostilas'
import { rotuloApostila } from '../lib/capitulos'
import EnunciadoQuestao, { LinhasResposta } from '../lib/EnunciadoQuestao'

function nomeCapitulo(id: string) {
  const a = apostilas.find((x) => x.id === id)
  return a ? `${rotuloApostila(a)} – ${a.titulo}` : id
}

/** linha do banco de questões: o caso ajuda a reconhecer a questão quando o enunciado é genérico */
function resumoQuestao(q: Questao) {
  const caso = q.caso?.[0] ?? q.contexto?.find((c) => c.t === 'p')?.texto
  if (!caso) return q.enunciado
  const curto = caso.length > 180 ? `${caso.slice(0, 180).trimEnd()}...` : caso
  return `${curto} ${q.enunciado}`
}

const TIPOS = ['P1', 'P2', '2ª Chamada', 'Prova final'] as const

/** linhas para resposta de cada questão discursiva (ou de cada item a, b, c...) na prova impressa */
const LINHAS_RESPOSTA = 4

/**
 * Cabeçalho no modelo da folha de prova (tabela com logos, aluno/período/matrícula,
 * professor(a)/disciplina, tipo/data/valor/nota e quadro de regras).
 * Os nomes e logos da instituição NÃO ficam no código do site: são digitados/enviados aqui
 * e guardados só no navegador de quem gera a prova.
 */
interface Cabecalho {
  /** uma linha por item; a última sai em negrito */
  instituicao: string
  logoEsquerda: string
  logoDireita: string
  professora: string
  disciplina: string
  periodo: string
  tipo: (typeof TIPOS)[number]
  data: string
  valor: string
  regras: string
}

const CAB_PADRAO: Cabecalho = {
  instituicao: '',
  logoEsquerda: '',
  logoDireita: '',
  professora: '',
  disciplina: '',
  periodo: '',
  tipo: 'P1',
  data: '',
  valor: '6,0',
  regras: [
    'É proibido soltar os grampos da prova;',
    'Não é permitido o empréstimo de material;',
    'A prova deve ser feita a caneta azul ou preta;',
    'Não é permitido o uso de celular dentro de sala de aula no decorrer da prova;',
    'Para as questões objetivas, as opções rasuradas serão desconsideradas.',
  ].join('\n'),
}

const CHAVE_CAB = 'tecpro-cabecalho-prova'

function lerCabecalho(): Cabecalho {
  try {
    return { ...CAB_PADRAO, ...JSON.parse(localStorage.getItem(CHAVE_CAB) ?? '{}') }
  } catch {
    return CAB_PADRAO
  }
}

const numero = (v: string) => Number(v.replace(',', '.')) || 0
const formatar = (n: number) => n.toLocaleString('pt-BR', { minimumFractionDigits: 1, maximumFractionDigits: 2 })

/** divide o valor total igualmente; a diferença do arredondamento vai para a última questão */
function dividir(total: number, n: number) {
  if (!n) return []
  const centavos = Math.round(total * 100)
  const parte = Math.floor(centavos / n)
  return Array.from({ length: n }, (_, i) => (i === n - 1 ? centavos - parte * (n - 1) : parte) / 100)
}

interface Versao {
  nome: string
  questoes: Questao[]
}

export default function GerarProva() {
  const [cab, setCab] = useState<Cabecalho>(lerCabecalho)
  const [filtro, setFiltro] = useState<Filtro>(FILTRO_VAZIO)
  const [selecionadas, setSelecionadas] = useState<string[]>([])
  const [valores, setValores] = useState<Record<string, string>>({})
  const [sortear, setSortear] = useState(5)
  const [numVersoes, setNumVersoes] = useState(1)
  const [embQuestoes, setEmbQuestoes] = useState(true)
  const [embAlternativas, setEmbAlternativas] = useState(true)
  const [versoes, setVersoes] = useState<Versao[] | null>(null)

  useEffect(() => {
    try {
      localStorage.setItem(CHAVE_CAB, JSON.stringify(cab))
    } catch {
      // sem armazenamento (ou logo grande demais): o cabeçalho vale só nesta visita
    }
  }, [cab])

  const visiveis = filtrar(questoes, filtro)
  const escolhidas = questoes.filter((q) => selecionadas.includes(q.id))
  const divisao = dividir(numero(cab.valor), escolhidas.length)
  const valorDe = (id: string) => {
    const i = escolhidas.findIndex((q) => q.id === id)
    return valores[id] ?? (i >= 0 ? formatar(divisao[i]) : '')
  }
  const somaValores = escolhidas.reduce((s, q) => s + numero(valorDe(q.id)), 0)

  const alternar = (id: string) =>
    setSelecionadas((s) => (s.includes(id) ? s.filter((x) => x !== id) : [...s, id]))

  function sortearQuestoes() {
    const novas = embaralhar(visiveis.filter((q) => !selecionadas.includes(q.id))).slice(0, sortear)
    setSelecionadas((s) => [...s, ...novas.map((q) => q.id)])
  }

  function gerar() {
    const lista: Versao[] = []
    for (let v = 0; v < numVersoes; v++) {
      let qs = embQuestoes ? embaralhar(escolhidas) : escolhidas
      if (embAlternativas) qs = qs.map(embaralharAlternativas)
      lista.push({ nome: numVersoes > 1 ? `Versão ${LETRAS[v]}` : '', questoes: qs })
    }
    setVersoes(lista)
    window.scrollTo(0, 0)
  }

  function carregarLogo(lado: 'logoEsquerda' | 'logoDireita', arquivo?: File) {
    if (!arquivo) return
    const leitor = new FileReader()
    leitor.onload = () => setCab((c) => ({ ...c, [lado]: String(leitor.result) }))
    leitor.readAsDataURL(arquivo)
  }

  const campo = (chave: 'professora' | 'disciplina' | 'periodo' | 'data' | 'valor', rotulo: string) => (
    <label>
      {rotulo}
      <input value={cab[chave]} onChange={(e) => setCab({ ...cab, [chave]: e.target.value })} />
    </label>
  )

  if (versoes) {
    const linhasInst = cab.instituicao.split('\n').filter((l) => l.trim())
    return (
      <>
        <div className="barra-acoes no-print">
          <button onClick={() => setVersoes(null)}>Voltar e editar</button>
          <button className="secundario" onClick={gerar}>
            Embaralhar de novo
          </button>
          <button onClick={() => window.print()}>Imprimir / salvar PDF</button>
        </div>

        {versoes.map((v) => (
          <article key={v.nome} className="folha prova-modelo">
            <div className="cab-modelo">
              {(linhasInst.length > 0 || cab.logoEsquerda || cab.logoDireita) && (
                <div className="cab-topo">
                  <div className="cab-logo">{cab.logoEsquerda && <img src={cab.logoEsquerda} alt="" />}</div>
                  <div className="cab-inst">
                    {linhasInst.map((l, i) => (
                      <div key={i} className={i === linhasInst.length - 1 ? 'negrito' : undefined}>
                        {l}
                      </div>
                    ))}
                  </div>
                  <div className="cab-logo">{cab.logoDireita && <img src={cab.logoDireita} alt="" />}</div>
                </div>
              )}
              <div className="cab-grade">
                <div className="c-nome">Nome do aluno (a):</div>
                <div className="c-periodo">
                  Período: <span className="normal">{cab.periodo}</span>
                </div>
                <div className="c-matricula">Matrícula:</div>
                <div className="c-professor">
                  Professor (a): <span className="normal">{cab.professora}</span>
                </div>
                <div className="c-disciplina">
                  Disciplina: <span className="normal">{cab.disciplina}</span>
                </div>
                <div className="c-tipo">
                  {TIPOS.map((t) => (
                    <span key={t}>
                      ({cab.tipo === t ? 'x' : '  '}) {t}{' '}
                    </span>
                  ))}
                  {v.nome && <span className="versao">{v.nome}</span>}
                </div>
                <div className="c-data">
                  Data:
                  <div className="normal centro">{cab.data}</div>
                </div>
                <div className="c-valor">
                  Valor:
                  <div className="normal centro">{cab.valor}</div>
                </div>
                <div className="c-nota">Nota:</div>
              </div>
              {cab.regras.trim() && (
                <div className="cab-regras">
                  {cab.regras
                    .split('\n')
                    .filter((l) => l.trim())
                    .map((l, i) => (
                      <div key={i}>- {l.replace(/^-\s*/, '')}</div>
                    ))}
                </div>
              )}
            </div>

            {v.questoes.map((q, n) => (
              <section key={q.id} className="questao-modelo">
                <div className="barra-questao">
                  <span>Questão {n + 1}</span>
                  <span className="valor-questao">Valor: {valorDe(q.id)}</span>
                </div>
                <EnunciadoQuestao
                  q={q}
                  linhasPorItem={q.tipo === 'discursiva' && !q.pratica ? LINHAS_RESPOSTA : undefined}
                />
                {q.tipo === 'objetiva' ? (
                  <ol className="alts-prova">
                    {q.alternativas.map((a, i) => (
                      <li key={i}>
                        {LETRAS[i]}) {a}
                      </li>
                    ))}
                  </ol>
                ) : q.pratica || q.itens?.length ? null : (
                  <LinhasResposta quantidade={LINHAS_RESPOSTA} />
                )}
              </section>
            ))}
          </article>
        ))}
      </>
    )
  }

  return (
    <>
      <h1>Gerar prova</h1>

      <section className="painel">
        <h2>1. Cabeçalho</h2>
        <p className="dica">
          A folha segue o modelo padrão de prova. O que você preencher aqui fica guardado só neste navegador, para as
          próximas provas, e não é publicado no site.
        </p>
        <label className="bloco">
          Instituição (uma linha por item; a última sai em negrito)
          <textarea
            rows={4}
            value={cab.instituicao}
            onChange={(e) => setCab({ ...cab, instituicao: e.target.value })}
          />
        </label>
        <div className="filtros">
          {(['logoEsquerda', 'logoDireita'] as const).map((lado) => (
            <label key={lado}>
              {lado === 'logoEsquerda' ? 'Logo da esquerda' : 'Logo da direita'}
              <input type="file" accept="image/*" onChange={(e) => carregarLogo(lado, e.target.files?.[0])} />
              {cab[lado] && (
                <span className="logo-escolhido">
                  <img src={cab[lado]} alt="" />
                  <button type="button" className="secundario" onClick={() => setCab({ ...cab, [lado]: '' })}>
                    Remover
                  </button>
                </span>
              )}
            </label>
          ))}
        </div>
        <div className="filtros">
          {campo('professora', 'Professor (a)')}
          {campo('disciplina', 'Disciplina')}
          {campo('periodo', 'Período')}
          {campo('data', 'Data')}
          {campo('valor', 'Valor da prova')}
          <label>
            Tipo
            <select value={cab.tipo} onChange={(e) => setCab({ ...cab, tipo: e.target.value as Cabecalho['tipo'] })}>
              {TIPOS.map((t) => (
                <option key={t}>{t}</option>
              ))}
            </select>
          </label>
        </div>
        <label className="bloco">
          Regras (uma por linha)
          <textarea rows={5} value={cab.regras} onChange={(e) => setCab({ ...cab, regras: e.target.value })} />
        </label>
      </section>

      <section className="painel">
        <h2>2. Questões ({selecionadas.length} selecionadas)</h2>
        <Filtros
          valor={filtro}
          onChange={(f) => {
            setFiltro(f)
            if (f.disciplinaId && !cab.disciplina) setCab({ ...cab, disciplina: nomeDisciplina(f.disciplinaId) })
          }}
        />
        <div className="barra-acoes">
          <label className="inline">
            Sortear
            <input type="number" min={1} value={sortear} onChange={(e) => setSortear(Math.max(1, Number(e.target.value)))} />
            questões do filtro
          </label>
          <button className="secundario" onClick={sortearQuestoes}>
            Sortear
          </button>
          <button className="secundario" onClick={() => setSelecionadas([])} disabled={!selecionadas.length}>
            Limpar seleção
          </button>
        </div>
        <ul className="banco">
          {visiveis.map((q) => (
            <li key={q.id}>
              <label>
                <input type="checkbox" checked={selecionadas.includes(q.id)} onChange={() => alternar(q.id)} />
                <span>
                  <span className="meta">
                    {nomeDisciplina(q.disciplinaId)} · {nomeCapitulo(q.capituloId)} ·{' '}
                    {q.tipo === 'objetiva' ? 'Objetiva' : 'Discursiva'}
                    {q.nivel && ` · ${NOMES_NIVEL[q.nivel]}`}
                  </span>
                  {resumoQuestao(q)}
                </span>
              </label>
            </li>
          ))}
        </ul>
        {visiveis.length === 0 && (
          <p className="dica">
            Ainda não há questões cadastradas para este filtro. Escolha outra disciplina ou outro capítulo (o número entre
            parênteses mostra quantas questões cada um tem).
          </p>
        )}
      </section>

      {escolhidas.length > 0 && (
        <section className="painel">
          <h2>3. Valor de cada questão</h2>
          <p className="dica">
            O valor da prova ({cab.valor}) é dividido igualmente; altere o que quiser. Soma atual: {formatar(somaValores)}
            {Math.abs(somaValores - numero(cab.valor)) > 0.001 && ' (diferente do valor da prova)'}
          </p>
          <ol className="valores-questoes">
            {escolhidas.map((q) => (
              <li key={q.id}>
                <input
                  value={valorDe(q.id)}
                  onChange={(e) => setValores({ ...valores, [q.id]: e.target.value })}
                  aria-label="Valor da questão"
                />
                <span>{resumoQuestao(q)}</span>
              </li>
            ))}
          </ol>
          {Object.keys(valores).length > 0 && (
            <button className="secundario" onClick={() => setValores({})}>
              Voltar à divisão igual
            </button>
          )}
        </section>
      )}

      <section className="painel">
        <h2>{escolhidas.length > 0 ? '4' : '3'}. Opções</h2>
        <div className="filtros">
          <label>
            Número de versões
            <select value={numVersoes} onChange={(e) => setNumVersoes(Number(e.target.value))}>
              {[1, 2, 3, 4].map((n) => (
                <option key={n}>{n}</option>
              ))}
            </select>
          </label>
        </div>
        <label className="inline">
          <input type="checkbox" checked={embQuestoes} onChange={(e) => setEmbQuestoes(e.target.checked)} />
          Embaralhar ordem das questões
        </label>
        <label className="inline">
          <input type="checkbox" checked={embAlternativas} onChange={(e) => setEmbAlternativas(e.target.checked)} />
          Embaralhar alternativas
        </label>
      </section>

      <button disabled={!selecionadas.length} onClick={gerar}>
        Gerar prova
      </button>
      {!selecionadas.length && (
        <p className="dica">Marque pelo menos uma questão na etapa 2, ou use o botão Sortear, para liberar o botão.</p>
      )}
    </>
  )
}
