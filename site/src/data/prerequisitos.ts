// Pré-requisitos das disciplinas da Graduação: para cursar a disciplina (a chave), o aluno
// precisa ter cursado antes todas as da lista. Sistemas para Internet: "Fluxograma das
// disciplinas de Pré-requisito da Matriz Curricular 2024", versão 2025.1 (FAETERJ Barra
// Mansa), lido em 23/10/2026. Disciplinas fora desta lista não têm pré-requisito.
// Usado no pedido de disciplina de outro período (lib/PedidosDisciplina.tsx).

export const PRE_REQUISITOS: Record<string, string[]> = {
  // 2º período
  'fundamentos-de-estruturas-de-dados': ['algoritmos-e-linguagem-de-programacao-i'],
  'algoritmos-e-linguagem-de-programacao-ii': ['algoritmos-e-linguagem-de-programacao-i'],
  'programacao-e-design-para-web-i': ['algoritmos-e-linguagem-de-programacao-i'],
  // 3º período
  'analise-e-projeto-de-sistemas': ['modelagem-conceitual-de-dados'],
  'gestao-de-projeto-de-banco-de-dados': ['modelagem-conceitual-de-dados', 'fundamentos-de-redes-de-computadores'],
  'programacao-e-design-para-web-ii': [
    'fundamentos-de-estruturas-de-dados',
    'algoritmos-e-linguagem-de-programacao-ii',
    'programacao-e-design-para-web-i',
  ],
  // 4º período
  'programacao-para-dispositivos-moveis': ['programacao-e-design-para-web-ii'],
  'programacao-cliente-servidor': ['programacao-e-design-para-web-ii', 'fundamentos-de-redes-de-computadores'],
  'empreendedorismo-digital': ['midias-digitais'],
  'gestao-de-sistemas-digitais-na-web': ['midias-digitais'],
  'projeto-integrador-i': ['metodologia-da-pesquisa-cientifico-tecnologica'],
  'projeto-de-extensao-ii': ['projeto-de-extensao-i'],
  // 5º período
  'programacao-e-design-para-web-iii': ['programacao-e-design-para-web-ii', 'programacao-cliente-servidor'],
  'projeto-integrador-ii': ['projeto-integrador-i'],
  'laboratorio-de-projeto-integrador-ii': ['projeto-integrador-i'],
  'projeto-de-extensao-iii': ['projeto-de-extensao-ii'],
}
