# Controle de Qualidade e Estocagem

Protótipo desenvolvido em Python para automatizar o controle de qualidade e a estocagem de peças fabricadas em uma linha de montagem industrial, substituindo a inspeção manual para reduzir falhas, atrasos e custos de operação.

---

##  Sobre o Projeto

O sistema simula a entradas de um humano na linha de produção industrial:
1. **Identificação Única:** Cada peça produzida recebe um ID randômico exclusivo (de 1 a 30.000), garantindo rastreabilidade sem duplicidade.
2. **Inspeção das caracteristicas:** Valida os atributos físicos (peso, cor e comprimento) segundo tolerâncias rigorosas.
3. **Empacotamento:** Peças aprovadas são direcionadas para caixas com capacidade de 10 peças. Quando uma caixa atinge a capacidade máxima, o sistema fecha a caixa atual, arquiva-a no lote de concluídas (caixas) e abre uma nova caixa automaticamente.
4. **Tratamento de Não Conformidades:** Peças reprovadas são arquivadas com o registro dos motivos da falha.
5. **Painel de Gestão:** Emite relatórios consolidados em tempo real com totais de peças e caixas.

---

## Critérios de Aceitação de Qualidade

Para ser **APROVADA**, a peça deve cumprir todos os critérios abaixo:

| **Peso** | Entre `95.0` e `105.0` | Gramas (g) |
| **Cor** | Azul (`A`) ou Verde (`V`) | 
| **Comprimento** | Entre `10.0` e `20.0` | Centímetros (cm) |

Caso qualquer critério não seja atendido, a peça é marcada como **REPROVADA** e o motivo específico é gravado no histórico.

---

## Funcionalidades do Sistema

O menu interativo conta com 6 opções operacionais:
- **`[1] Nova peca`:** Cadastra as características físicas da peça, executa a validação e faz a destinação correta (caixa ou reprovada).
- **`[2] Aprovadas/reprovadas`:** Exibe a relação detalhada de todas as peças auditadas.
- **`[3] Remover peça`:** Remove uma peça do sistema por meio do seu ID (busca nas listas de aprovadas, reprovadas, caixa aberta e caixas fechadas).
- **`[4] Caixas`:** Lista todos os lotes de caixas fechadas (com 10 peças).
- **`[5] Relatorio Final`:** Exibe os totais de produção.
- **`[6] Sair`:** Encerra a execução do programa.

---

## Como Rodar o Programa

### Pré-requisitos
- **Python 3.10 ou superior** instalado (necessário devido ao uso de estruturas `match/case`).
- Terminal compatível com Windows (PowerShell ou Prompt de Comando).

### Passo a Passo

1. **Abra o terminal** no diretório do projeto:
   ```powershell
   cd "c:\Unifecaf\Logica de Programacao Python\PadraoDeProducao"
   ```

2. **Execute o script principal:**
   ```powershell
   python main.py
   ```
   *(ou `py main.py` dependendo da instalação do Python no seu computador)*

3. **Interaja com o Menu:**
   O menu interativo será exibido na tela. Digite o número correspondente à opção desejada e pressione `Enter`.

---

## Exemplos de Entradas e Saídas

### 1. Menu Principal
```
|-----------------------------------------------------------------------------------------------------------|
| [1] Nova peca  | [2] Aprovadas/reprovadas | [3] Remover peça | [4] Caixas | [5] Relatorio Final| [6] Sair |
|-----------------------------------------------------------------------------------------------------------|
1
```

---

### 2. Cadastro de Peça Aprovada (Opção 1)
**Entrada do Usuário:**
```
---- ID GERADO: 14820 ----
Qual o peso da peça? 100.5
Qual a cor da peça? [A] | [V] | [O-Outra]: a
Qual o comprimento da peça? 15.2
```
**Resultado:** Como todos os valores estão dentro da tolerância, a peça é aprovada silenciosamente e guardada na caixa em aberto. O sistema retorna ao menu principal.

---

### 3. Cadastro de Peça Reprovada (Opção 1)
**Entrada do Usuário:**
```
---- ID GERADO: 27315 ----
Qual o peso da peça? 88.0
Qual a cor da peça? [A] | [V] | [O-Outra]: o
Qual o comprimento da peça? 25.0
```
**Saída no Terminal:**
```
Peça [27315] foi REPROVADA!
Motivo(s): [Peso incorreto | Cor incorreta | Comprimento incorreto | ]
Pressione qualquer tecla para continuar. . .
```

---

### 4. Consulta de Peças Aprovadas e Reprovadas (Opção 2)
**Seleção:** Opção `2`  
**Saída no Terminal:**
```text
APROVADAS:
[[14820, 100.5, 'A', 15.2, '']]

REPROVADAS:
[[27315, 88.0, 'O', 25.0, 'Peso incorreto | Cor incorreta | Comprimento incorreto | ']]
Pressione qualquer tecla para continuar. . .
```

---

### 5. Remoção de Peça por ID (Opção 3)
**Seleção:** Opção `3`  
**Entrada do Usuário:**
```text
Qual ID quer remover: 27315
```
**Saída no Terminal:**
```text
[[27315, 88.0, 'O', 25.0, 'Peso incorreto | Cor incorreta | Comprimento incorreto | ']] foi removida
Pressione qualquer tecla para continuar. . .
```

---

### 6. Relatório Final de Produção (Opção 5)
**Seleção:** Opção `5`  
**Saída no Terminal:**
```text
Total de peças aprovadas: 11
Total de peças reprovadas: 2
Total de caixas fechadas: 1
Caixa atual (em aberto): [[2981, 101.0, 'V', 12.0, '']]
Pressione qualquer tecla para continuar. . .
```

---

## Estrutura dos Arquivos

```
|-- main.py                 # Código-fonte principal com menu e lógica operacional
|-- README.md               # Instruções de execução e documentação do projeto
|-- PROJETO_AUTOMACAO_INDUSTRIAL.md     # Contextualização sobre o desafio da automação industrial
```
