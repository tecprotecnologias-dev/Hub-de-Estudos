import { useEffect, useState } from 'react'
import { Link, useParams } from 'react-router-dom'
import { apostilas } from '../data/apostilas'
import { disciplinas } from '../data/disciplinas'
import { questoes } from '../data/questoes'
import type { Apostila, QuestaoDiscursiva, QuestaoObjetiva } from '../data/tipos'
import { apostilasDaDisciplina, rotuloApostila } from '../lib/capitulos'
import EnunciadoQuestao, { Resolucao } from '../lib/EnunciadoQuestao'
import { verificarCodigo } from '../lib/verificarCodigo'
import { buscarDisciplina, embaralhar, embaralharAlternativas, LETRAS, nomePeriodo, PERIODOS } from '../lib/util'

// Estrutura da aba:
//   /simulado                                  -> disciplinas
//   /simulado/:disciplinaId                    -> capítulos, cada um com Objetivas e Discursivas
//   /simulado/:disciplinaId/:capituloId/:tipo  -> as questões (tipo = objetivas | discursivas)

const objetivasDo = (capituloId: string) =>
  questoes.filter((q): q is QuestaoObjetiva => q.capituloId === capituloId && q.tipo === 'objetiva')
const discursivasDo = (capituloId: string) =>
  questoes.filter((q): q is QuestaoDiscursiva => q.capituloId === capituloId && q.tipo === 'discursiva')
const plural = (n: number, um: string, varios: string) => `${n} ${n === 1 ? um : varios}`

export default function Simulado() {
  const { disciplinaId, capituloId, tipo } = useParams()
  if (disciplinaId && capituloId && tipo) {
    const cap = apostilas.find((a) => a.id === capituloId && a.disciplinaId === disciplinaId)
    if (!cap) return <NaoEncontrado />
    return tipo === 'objetivas' ? <Objetivas key={cap.id} cap={cap} /> : <Discursivas key={cap.id} cap={cap} />
  }
  if (disciplinaId) return <Capitulos disciplinaId={disciplinaId} />
  return <ListaDisciplinas />
}

function NaoEncontrado() {
  return (
    <>
      <h1>Simulado não encontrado</h1>
      <Link to="/simulado">Voltar para os simulados</Link>
    </>
  )
}

/* ---------------------------------------------------------------- disciplinas */

function ListaDisciplinas() {
  return (
    <>
      <h1>Simulados</h1>
      <p className="dica">Escolha a disciplina. As questões estão organizadas pelos capítulos da apostila.</p>
      {PERIODOS.map((p) => {
        const doPeriodo = disciplinas.filter((d) => d.periodo === p)
        if (!doPeriodo.length) return null
        return (
          <section key={p} className="bloco-periodo">
            <h2>{nomePeriodo(p)}</h2>
            <div className="cartoes">
              {doPeriodo.map((d) => {
                // sem apostila ainda não há capítulos para organizar as questões
                if (!apostilasDaDisciplina(d.id).length) {
                  return (
                    <div key={d.id} className="cartao cartao-em-breve">
                      <h3>{d.nome}</h3>
                      <p className="contagens-simulado">
                        <span className="dica">Simulado em preparação</span>
                      </p>
                    </div>
                  )
                }
                const nObj = questoes.filter((q) => q.disciplinaId === d.id && q.tipo === 'objetiva').length
                const nDis = questoes.filter((q) => q.disciplinaId === d.id && q.tipo === 'discursiva').length
                return (
                  <Link key={d.id} to={`/simulado/${d.id}`} className="cartao">
                    <h3>{d.nome}</h3>
                    <p className="contagens-simulado">
                      {nObj + nDis === 0 ? (
                        <span className="dica">Questões em preparação</span>
                      ) : (
                        <>
                          <span>{plural(nObj, 'objetiva', 'objetivas')}</span>
                          <span>{plural(nDis, 'discursiva', 'discursivas')}</span>
                        </>
                      )}
                    </p>
                  </Link>
                )
              })}
            </div>
          </section>
        )
      })}
    </>
  )
}

/* ---------------------------------------------------------------- capítulos */

function Capitulos({ disciplinaId }: { disciplinaId: string }) {
  const d = buscarDisciplina(disciplinaId)
  if (!d) return <NaoEncontrado />
  // guias e infográficos (material sem número de capítulo/módulo) não têm questões, e o material
  // complementar (cadastrado com grupo) é só para estudo: só entra se tiver questões próprias
  const caps = apostilasDaDisciplina(d.id).filter(
    (a) => a.capitulo != null && (!a.grupo || questoes.some((q) => q.capituloId === a.id)),
  )
  return (
    <>
      <Link to="/simulado" className="voltar">
        Todas as disciplinas
      </Link>
      <p className="etiqueta">{nomePeriodo(d.periodo)}</p>
      <h1>Simulados – {d.nome}</h1>
      <p className="dica">Escolha o capítulo e o tipo de questão.</p>
      <ul className="lista-simulado">
        {caps.map((a) => {
          const nObj = objetivasDo(a.id).length
          const discursivas = discursivasDo(a.id)
          const nDis = discursivas.length
          const soPraticas = nDis > 0 && discursivas.every((q) => q.pratica)
          return (
            <li key={a.id}>
              <div>
                <span className="etiqueta">{rotuloApostila(a)}</span>
                <strong>{a.titulo}</strong>
              </div>
              <div className="botoes-simulado">
                {nObj > 0 ? (
                  <Link className="botao" to={`/simulado/${d.id}/${a.id}/objetivas`}>
                    Objetivas ({nObj})
                  </Link>
                ) : (
                  <span className="botao desativado">Objetivas (0)</span>
                )}
                {nDis > 0 ? (
                  <Link className="botao secundario" to={`/simulado/${d.id}/${a.id}/discursivas`}>
                    {soPraticas ? 'Exercícios práticos' : 'Discursivas'} ({nDis})
                  </Link>
                ) : (
                  <span className="botao secundario desativado">Discursivas (0)</span>
                )}
              </div>
            </li>
          )
        })}
      </ul>
    </>
  )
}

function Cabecalho({ cap, tipo }: { cap: Apostila; tipo: string }) {
  const d = buscarDisciplina(cap.disciplinaId)
  return (
    <>
      <Link to={`/simulado/${cap.disciplinaId}`} className="voltar">
        {d?.nome}
      </Link>
      <p className="etiqueta">
        {rotuloApostila(cap)} · {tipo}
      </p>
      <h1>{cap.titulo}</h1>
    </>
  )
}

/* ---------------------------------------------------------------- objetivas */

interface Registro {
  data: string
  acertos: number
  total: number
  descricao: string
}

const CHAVE_HISTORICO = 'tecpro-historico'

function lerHistorico(): Registro[] {
  try {
    return JSON.parse(localStorage.getItem(CHAVE_HISTORICO) ?? '[]')
  } catch {
    return []
  }
}

function salvarNoHistorico(r: Registro) {
  try {
    localStorage.setItem(CHAVE_HISTORICO, JSON.stringify([r, ...lerHistorico()].slice(0, 20)))
  } catch {
    // sem armazenamento disponível: o histórico simplesmente não é salvo
  }
}

function formatarTempo(seg: number) {
  return `${Math.floor(seg / 60)}:${String(seg % 60).padStart(2, '0')}`
}

function Objetivas({ cap }: { cap: Apostila }) {
  const banco = objetivasDo(cap.id)
  const [etapa, setEtapa] = useState<'config' | 'fazendo' | 'resultado'>('config')
  const [quantidade, setQuantidade] = useState(Math.min(10, banco.length))
  const [minutos, setMinutos] = useState(0)
  const [prova, setProva] = useState<QuestaoObjetiva[]>([])
  const [respostas, setRespostas] = useState<Record<string, number>>({})
  const [restante, setRestante] = useState(0)
  const [historico, setHistorico] = useState<Registro[]>(lerHistorico)

  function iniciar() {
    setProva(embaralhar(banco).slice(0, quantidade).map((q) => embaralharAlternativas(q) as QuestaoObjetiva))
    setRespostas({})
    setRestante(minutos * 60)
    setEtapa('fazendo')
    window.scrollTo(0, 0)
  }

  function finalizar() {
    const acertos = prova.filter((q) => respostas[q.id] === q.correta).length
    salvarNoHistorico({
      data: new Date().toLocaleString('pt-BR'),
      acertos,
      total: prova.length,
      descricao: `${buscarDisciplina(cap.disciplinaId)?.nome} – ${rotuloApostila(cap)}`,
    })
    setHistorico(lerHistorico())
    setEtapa('resultado')
    window.scrollTo(0, 0)
  }

  // cronômetro regressivo (só quando o simulado tem tempo definido)
  useEffect(() => {
    if (etapa !== 'fazendo' || minutos === 0) return
    if (restante <= 0) {
      finalizar()
      return
    }
    const t = setTimeout(() => setRestante((r) => r - 1), 1000)
    return () => clearTimeout(t)
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [etapa, restante])

  if (etapa === 'config') {
    return (
      <>
        <Cabecalho cap={cap} tipo="Questões objetivas" />
        <p className="dica">{plural(banco.length, 'questão disponível', 'questões disponíveis')} neste capítulo.</p>
        <div className="filtros">
          <label>
            Quantidade de questões
            <input
              type="number"
              min={1}
              max={banco.length}
              value={quantidade}
              onChange={(e) => setQuantidade(Math.min(banco.length, Math.max(1, Number(e.target.value))))}
            />
          </label>
          <label>
            Tempo (minutos, 0 = sem limite)
            <input type="number" min={0} value={minutos} onChange={(e) => setMinutos(Math.max(0, Number(e.target.value)))} />
          </label>
        </div>
        <button disabled={banco.length === 0} onClick={iniciar}>
          Começar simulado
        </button>

        {historico.length > 0 && (
          <section className="historico">
            <h2>Seus últimos simulados</h2>
            <table>
              <thead>
                <tr>
                  <th>Data</th>
                  <th>Conteúdo</th>
                  <th>Acertos</th>
                </tr>
              </thead>
              <tbody>
                {historico.map((r, i) => (
                  <tr key={i}>
                    <td>{r.data}</td>
                    <td>{r.descricao}</td>
                    <td>
                      {r.acertos}/{r.total} ({Math.round((r.acertos / r.total) * 100)}%)
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </section>
        )}
      </>
    )
  }

  const respondidas = Object.keys(respostas).length
  const acertos = prova.filter((q) => respostas[q.id] === q.correta).length
  const corrigindo = etapa === 'resultado'

  return (
    <>
      <Cabecalho cap={cap} tipo="Questões objetivas" />
      {corrigindo ? (
        <section className="resultado">
          <h2>Resultado</h2>
          <p className="nota">
            {acertos} de {prova.length} ({Math.round((acertos / prova.length) * 100)}%)
          </p>
          <div className="barra-acoes">
            <button onClick={() => setEtapa('config')}>Fazer de novo</button>
            <Link className="botao secundario" to={`/simulado/${cap.disciplinaId}`}>
              Outros capítulos
            </Link>
          </div>
        </section>
      ) : (
        <div className="barra-simulado">
          <span>
            {respondidas} de {prova.length} respondidas
          </span>
          {minutos > 0 && <span className={restante < 60 ? 'tempo alerta' : 'tempo'}>{formatarTempo(restante)}</span>}
        </div>
      )}

      <ol className="lista-questoes">
        {prova.map((q) => {
          const marcada = respostas[q.id]
          return (
            <li key={q.id} className="questao">
              <EnunciadoQuestao q={q} />
              <div className="alternativas">
                {q.alternativas.map((alt, i) => {
                  let classe = 'alternativa'
                  if (marcada === i) classe += ' marcada'
                  if (corrigindo && i === q.correta) classe += ' certa'
                  if (corrigindo && marcada === i && i !== q.correta) classe += ' errada'
                  return (
                    <label key={i} className={classe}>
                      <input
                        type="radio"
                        name={q.id}
                        disabled={corrigindo}
                        checked={marcada === i}
                        onChange={() => setRespostas({ ...respostas, [q.id]: i })}
                      />
                      <strong>{LETRAS[i]})</strong> {alt}
                    </label>
                  )
                })}
              </div>
              {corrigindo && (
                <div className="correcao">
                  {marcada === undefined ? 'Não respondida. ' : marcada === q.correta ? 'Acertou. ' : 'Errou. '}
                  Resposta: {LETRAS[q.correta]}.{q.resolucao && <> {q.resolucao}</>}
                </div>
              )}
            </li>
          )
        })}
      </ol>

      {!corrigindo && (
        <button onClick={finalizar}>
          Entregar simulado{respondidas < prova.length && ` (${prova.length - respondidas} em branco)`}
        </button>
      )}
    </>
  )
}

/* ---------------------------------------------------------------- discursivas */

function Discursivas({ cap }: { cap: Apostila }) {
  const banco = discursivasDo(cap.id)
  if (banco.length > 0 && banco.every((q) => q.pratica)) return <ListaPratica cap={cap} banco={banco} />
  return <DiscursivasComResposta cap={cap} banco={banco} />
}

/* ---------------------------------------------------------------- lista prática */

// Exercícios práticos: o aluno escreve o código de cada exercício e só vê o gabarito
// (no fim da página) depois de finalizar a lista. O site não corrige: o aluno compara.
// Os códigos e o estado da lista ficam no navegador (localStorage), por capítulo.

interface EstadoLista {
  codigos: Record<string, string>
  finalizada: boolean
}

const NIVEIS: Record<string, string> = { facil: 'Fácil', medio: 'Médio', dificil: 'Desafio' }

function lerLista(chave: string): EstadoLista {
  try {
    const salvo = JSON.parse(localStorage.getItem(chave) ?? 'null')
    if (salvo && typeof salvo === 'object') return { codigos: salvo.codigos ?? {}, finalizada: !!salvo.finalizada }
  } catch {
    // armazenamento indisponível ou corrompido: começa do zero
  }
  return { codigos: {}, finalizada: false }
}

// O site não executa o código: verificarCodigo só confere se o texto parece código, em qualquer
// linguagem. Isso barra letras, números e frases soltas, mas não diz se a solução está certa.

/** Tab insere quatro espaços em vez de sair da caixa (Shift+Tab continua saindo). */
function tabComoEspacos(e: React.KeyboardEvent<HTMLTextAreaElement>, mudar: (texto: string) => void) {
  if (e.key !== 'Tab' || e.shiftKey) return
  e.preventDefault()
  const caixa = e.currentTarget
  const { selectionStart: ini, selectionEnd: fim, value } = caixa
  mudar(value.slice(0, ini) + '    ' + value.slice(fim))
  requestAnimationFrame(() => caixa.setSelectionRange(ini + 4, ini + 4))
}

function ListaPratica({ cap, banco }: { cap: Apostila; banco: QuestaoDiscursiva[] }) {
  const chave = `tecpro-lista-${cap.id}`
  const [estado, setEstado] = useState<EstadoLista>(() => lerLista(chave))

  useEffect(() => {
    try {
      localStorage.setItem(chave, JSON.stringify(estado))
    } catch {
      // sem armazenamento: a lista funciona, só não fica salva
    }
  }, [chave, estado])

  const codigo = (id: string) => estado.codigos[id] ?? ''
  const verificacoes = banco.map((q) => verificarCodigo(codigo(q.id)))
  const pendentes = banco.map((_, i) => i + 1).filter((n) => !verificacoes[n - 1].ok)
  const completa = pendentes.length === 0
  // o gabarito só aparece com a lista completa (protege também um estado antigo salvo no navegador)
  const mostrarGabarito = estado.finalizada && completa

  function escrever(id: string, texto: string) {
    setEstado((e) => ({ ...e, codigos: { ...e.codigos, [id]: texto } }))
  }

  function finalizar() {
    if (!completa) return
    setEstado((e) => ({ ...e, finalizada: true }))
    requestAnimationFrame(() => document.getElementById('gabarito')?.scrollIntoView({ behavior: 'smooth' }))
  }

  function refazer() {
    if (!window.confirm('Apagar os seus códigos e esconder o gabarito para fazer a lista de novo?')) return
    setEstado({ codigos: {}, finalizada: false })
    window.scrollTo({ top: 0 })
  }

  return (
    <>
      <Cabecalho cap={cap} tipo="Exercícios práticos" />
      <p className="dica">
        Resolva cada exercício no seu computador, teste com os exemplos e cole o seu código na caixa. O gabarito só
        aparece no fim da página quando todas as caixas tiverem código. O que você escreve fica salvo apenas neste
        navegador.
      </p>
      <ol className="lista-questoes lista-exercicios">
        {banco.map((q, i) => (
          <li key={q.id} className="questao">
            {q.nivel && <p className="etiqueta">{NIVEIS[q.nivel]}</p>}
            <EnunciadoQuestao q={q} />
            <label className="rotulo-codigo" htmlFor={`codigo-${q.id}`}>
              Seu código
            </label>
            <textarea
              id={`codigo-${q.id}`}
              className="codigo-aluno"
              rows={10}
              spellCheck={false}
              placeholder="Cole ou escreva aqui o seu algoritmo..."
              value={codigo(q.id)}
              readOnly={mostrarGabarito}
              aria-describedby={`situacao-${q.id}`}
              onChange={(e) => escrever(q.id, e.target.value)}
              onKeyDown={(e) => tabComoEspacos(e, (t) => escrever(q.id, t))}
            />
            <p id={`situacao-${q.id}`} className={verificacoes[i].ok ? 'situacao-codigo ok' : 'situacao-codigo'}>
              {verificacoes[i].mensagem}
            </p>
          </li>
        ))}
      </ol>

      {!mostrarGabarito ? (
        <div className="finalizar-lista">
          <p className="dica">
            {completa
              ? 'Todos os exercícios têm código. Quando quiser, finalize para conferir com o gabarito.'
              : `${banco.length - pendentes.length} de ${banco.length} exercícios com código. Falta: ${pendentes
                  .map((n) => `exercício ${n}`)
                  .join(', ')}.`}
          </p>
          <button onClick={finalizar} disabled={!completa}>
            Finalizar e ver o gabarito
          </button>
        </div>
      ) : (
        <section id="gabarito" className="gabarito">
          <h2>Gabarito</h2>
          <p className="dica">
            Compare cada solução com o seu código. Há vários jeitos corretos de resolver: o que importa é o seu programa
            dar as saídas dos exemplos.
          </p>
          <ol className="lista-gabarito">
            {banco.map((q, i) => (
              <li key={q.id} className="questao-gabarito">
                <h3>Exercício {i + 1}</h3>
                <p className="rotulo-codigo">Seu código</p>
                <pre className="bloco-codigo codigo-do-aluno">
                  <code>{codigo(q.id)}</code>
                </pre>
                <p className="rotulo-codigo">Solução</p>
                {q.resolucao && <Resolucao partes={q.resolucao} />}
              </li>
            ))}
          </ol>
          <button className="secundario" onClick={refazer}>
            Refazer a lista
          </button>
        </section>
      )}
    </>
  )
}

/* ---------------------------------------------------------------- discursivas */

function DiscursivasComResposta({ cap, banco }: { cap: Apostila; banco: QuestaoDiscursiva[] }) {
  const [abertas, setAbertas] = useState<Record<string, boolean>>({})

  return (
    <>
      <Cabecalho cap={cap} tipo="Questões discursivas" />
      <p className="dica">
        {banco.length > 0 && banco.every((q) => q.pratica)
          ? 'Exercícios práticos: faça no seu computador e depois compare com a resolução passo a passo.'
          : 'Escreva sua resposta e depois compare com a resposta esperada. O que você escreve fica só no seu navegador e não é enviado.'}
      </p>
      {banco.length === 0 && <p className="vazio">Ainda não há questões discursivas neste capítulo.</p>}
      <ol className="lista-questoes">
        {banco.map((q) => (
          <li key={q.id} className="questao">
            {q.pratica && <p className="etiqueta">Exercício prático</p>}
            <EnunciadoQuestao q={q} />
            {q.pratica ? (
              <p className="dica">Faça no seu computador e depois compare com a resolução.</p>
            ) : (
              <textarea className="resposta-aluno" rows={5} placeholder="Escreva sua resposta aqui..." />
            )}
            {(q.respostaEsperada || q.resolucao) && (
              <>
                <button className="secundario" onClick={() => setAbertas({ ...abertas, [q.id]: !abertas[q.id] })}>
                  {abertas[q.id] ? 'Esconder' : q.resolucao ? 'Ver resolução' : 'Ver resposta esperada'}
                </button>
                {abertas[q.id] && q.respostaEsperada && (
                  <div className="correcao resposta-esperada">{q.respostaEsperada}</div>
                )}
                {abertas[q.id] && q.resolucao && <Resolucao partes={q.resolucao} />}
              </>
            )}
          </li>
        ))}
      </ol>
    </>
  )
}
