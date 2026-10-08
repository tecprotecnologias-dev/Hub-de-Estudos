import type { Questao } from './tipos'

// Banco de questões dos simulados e do gerador de provas.
//
// Cada questão pertence a um capítulo/módulo de apostila (capituloId = id em src/data/apostilas.ts)
// e é de um de dois tipos:
//
//   Objetiva:
//   {
//     id: 'engsoft-cap1-o1', disciplinaId: 'engenharia-de-software-e-da-usabilidade', capituloId: 'engsoft-cap1',
//     tipo: 'objetiva',
//     enunciado: 'Qual modelo de desenvolvimento ...?',
//     alternativas: ['Cascata', 'Espiral', 'Incremental', 'Scrum'],
//     correta: 0,                        // 0 = A, 1 = B, 2 = C ...
//     resolucao: 'Explicação mostrada depois da entrega.',
//   },
//
//   Discursiva:
//   {
//     id: 'engsoft-cap1-d1', disciplinaId: 'engenharia-de-software-e-da-usabilidade', capituloId: 'engsoft-cap1',
//     tipo: 'discursiva',
//     enunciado: 'Explique a diferença entre ...',
//     respostaEsperada: 'Texto que o aluno vê ao clicar em "Ver resposta esperada".',
//   },
//
// As questões convertidas dos Words de prova (ferramentas/converter_questoes.py) ficam em
// src/data/questoes/<disciplina>.json e entram aqui automaticamente.
const arquivos = import.meta.glob<Questao[]>('./questoes/*.json', { eager: true, import: 'default' })

export const questoes: Questao[] = Object.values(arquivos).flat()
