# Projeto: Sistema de Controle de Qualidade e Automação Industrial

---

## 1. Contextualização do Desafio

Hoje em dia, quase toda indústria vive sob pressão pra ser mais eficiente, competitiva e manter a qualidade em dia. E durante muito tempo, quem fazia a inspeção e triagem das peças nas linhas de produção eram pessoas, de forma manual.

O problema é que esse método manual tem limites claros:

- **Cansaço e subjetividade:** depois de horas repetindo a mesma tarefa, qualquer operador erra mais e fica menos consistente na avaliação.
- **Lentidão:** checar peça por peça na mão deixa a linha mais devagar e limita o quanto se consegue produzir.
- **Custo alto do erro:** uma peça com defeito que passa despercebida vira retrabalho, devolução, cliente insatisfeito e prejuízo pra reputação da marca.

É por isso que a automação digital deixou de ser luxo e virou praticamente obrigação pra quem quer entrar na lógica da **Indústria 4.0** — coletando dados em tempo real, validando peças automaticamente e controlando a expedição sem depender só de gente.

---

## 2. Como Estruturei o Raciocínio Lógico

A ideia foi usar um alogica simmples de facil adptação em projeto real com sensores e IA. O fluxo do sistema segue basicamente 4 etapas:

1. **Entrada e identificação** — gera um ID único pra cada peça e registra peso, cor e comprimento.
2. **Processamento e validação** — compara esses dados com os critérios aceitos pela fabrica.
3. **Armazenamento** — segrega aprovado e guarda, do que foi reprovado (fica registrado com o motivo).
4. **Consulta e relatório final** — permite consultar as caixas completadas, ver peças por aprovação e reprovação e ver o resumo geral da produção.

Para as funções:O Codigo foi dividido de forma a cada uma a responsabilidade de (gerarID, validaPeca, listaAprovadaReprovada, removePeca, caixasFechadas, relatorioFinal), evitando repetir lógica em vários lugares, algo bem calro em removePeca. 

Uso de match/case nas decisões:Usei a estrutura case para controlar o menu, cada opção cai num bloco isolado, e qualquer entrada inválida é tratada sem travar o programa. Já a validação da peça depende de três condições precisarem ser verdadeiras ao mesmo tempo (peso entre 95g e 105g, cor azul ou verde, comprimento entre 10cm e 20cm); se alguma falhar, o motivo específico é gravada peça, regravando nela todos os dados. E pra decidir se a peça aprovada vai pra caixa atual ou se abre uma caixa nova, o sistema simplesmente checa se já tem 10 peças ali dentro.

Loop do sistema com  while: Os laços de repetição cuidam de três coisas, manter o menu rodando até o usuário sair, gerar um ID novo até achar um que ainda não existe na lista (com a função gerarID), e percorrer listas (inclusive as caixas já fechadas) pra buscar(nos menus de relatorio) e remover uma peça específica(removePeca).

Cada peça, no fim das contas, é só uma lista com ID, peso, cor, comprimento e motivo de reprovação — simples assim.

---

## 3. Benefícios e Desafios

**O que a solução trouxe de bom:**

- Cada peça tem um ID rastreável, o que facilita auditoria e permite rastreio pela lista de IDs.
- O empacotamento virou automático: ao bater 10 peças, a caixa fecha sozinha e abre uma nova.
- Quando uma peça é reprovada, o motivo fica registrado na hora, isso vai ajudar a entender os problemas mais recorrentes.
- Os relatórios ficam disponíveis na hora, sem precisar esperar a caixa encherem ou acabar as peças de entrada.

**O que deu trabalho pra resolver:**

- Garantir que o ID sorteado nunca se repetisse, sem cair num loop infinito quando a lista ainda tava vazia — resolvido mantendo uma lista auxiliar apenas com os IDs ja criados, essa lista nao é alterada pela removePeca, logo permite uma audotoria.
- Como cada peça é uma lista com vários dados dentro, comparar pelo item inteiro não funcionava pra buscar por ID — precisei padronizar pra comparar sempre pela posição certa (`peca[0]`).
- Fechar a caixa certinho ao chegar em 10 peças, sem perder nem duplicar a peça que tava sendo processada naquele momento, exigiu cuidado na ordem das operações de limpeza da caixa e gravação nas listas certas.

---

## 4. Reflexão Final: Expandindo pra um Cenário Real

Esse protótipo em Python, rodando no terminal, já prova que a lógica de negócio funciona. Mas numa fábrica de verdade, dentro da lógica da Indústria 4.0, esse mesmo núcleo lógico poderia ganhar vida com hardware e sistemas de verdade:

- **Visão computaciona, IA e Sensores:**Em vez de usar entradas manuais, diretamente aa esterira de produção, balanças, sensores opticos de cor e comprimento, e cameras com IA para detecção de defeitos seriam usados para capturar os dados das peças, um sistema de visão computacional.
- **Automação eletromecânica:** a decisão do software se transformaria em ação física, pistões pneumáticos desviando peça reprovada, braços robóticos empacotando as aprovadas e fechando a caixa automaticamente.
- **Integração com sistemas:** os dados iriam pra um banco de verdade, se conectando a sistemas ERP e alimentando dashboards em tempo real na fábrica.

