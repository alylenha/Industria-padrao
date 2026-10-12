"""
PROJETO: CONTROLE DE QUALIDADE E ESTOCAGEM
-----------------------------------------------------------------
Solicitação:
Sistema para controlar a qualidade e a estocagem
de peças produzidas em uma linha de produção.

Requisitos:
# Coleta de dados por peça: ID, Peso (g), Cor (Azul ou Verde) e Comprimento (cm).
# Critérios de aprovação automática:
    - Peso: entre 95g e 105g
    - Cor: Azul(A) ou Verde(V)
    - Comprimento: entre 10cm e 20cm
# Armazenamento: Caixas com capacidade de até 10 peças aprovadas por caixa.
# Fechamento automático de caixas ao atingir a capacidade máxima e abertura de nova caixa.
# Relatórios consolidados:
    - Total de peças aprovadas
    - Total de peças reprovadas e respectivos motivos
    - Quantidade de caixas utilizadas
# Menu Interativo com 6 opções totalmente funcionais:
    [1] Cadastrar nova peça
    [2] Listar peças aprovadas/reprovadas
    [3] Remover peça cadastrada
    [4] Listar caixas fechadas
    [5] Gerar relatório final
    [6] Sair
"""

import sys
import time
import random
from os import system

# -----------------------------------------------------------------------------
# ESTRUTURAS DE DADOS GLOBAIS
# -----------------------------------------------------------------------------
# Estrutura base representativa dos atributos da peça: [id, peso, cor, comprimento, motivo]
peca = ['id', 'peso', 'cor', 'comprimento', 'motivo']

# Listas de controle de produção e expedição
listaIds = []   # Histórico de IDs gerados para garantir unicidade e validação de exclusão
caixa = []      # Caixa em uso no momento (armazena até 10 peças aprovadas)
caixas = []     # Lista com todas as caixas já fechadas (lotes concluídos)
aprovado = []   # Peças que atenderam a todos os critérios de qualidade
reprovado = []  # Peças fora do padrão (com o motivo da não conformidade registrado)


# -----------------------------------------------------------------------------
# FUNÇÕES DO SISTEMA
# -----------------------------------------------------------------------------
def gerarid(listaIds):
    """
    Gera automaticamente um ID numérico aleatório entre 1 e 30000.
    Garante que não existam IDs duplicados no histórico de produção.
    """
    while True:
        novo_id = random.randint(1, 30000)
        if novo_id not in listaIds:
            return novo_id


def validaPeca(peca):
    """
    Avalia automaticamente se a peça está aprovada ou reprovada
    segundo os critérios técnicos pré-definidos:
      - Peso entre 95g e 105g
      - Cor Azul ('A') ou Verde ('V')
      - Comprimento entre 10cm e 20cm
    Retorna a peça. Caso reprovada, anota os motivos em peca[4].
    """
    if peca[1] >= 95 and peca[1] <= 105 and peca[2] in ('A', 'V') and peca[3] >= 10 and peca[3] <= 20:
        return peca
    else:
        # Registra detalhadamente cada critério que não foi atendido
        if peca[1] < 95 or peca[1] > 105:
            peca[4] += 'Peso incorreto | '
        if peca[2] not in ('A', 'V'):
            peca[4] += 'Cor incorreta | '
        if peca[3] < 10 or peca[3] > 20:
            peca[4] += 'Comprimento incorreto | '
        return peca


def listaAprovadaReprovada(aprovado, reprovado):
    """
    Exibe a listagem completa de peças aprovadas e reprovadas,
    permitindo auditoria de qualidade na linha de produção.
    """
    print(f"APROVADAS:\n{aprovado}")
    print(f"\nREPROVADAS:\n{reprovado}")


def removePeca(lista, id):
    """
    Localiza e remove uma peça específica pelo seu ID (índice 0)
    dentro da lista indicada (aprovadas, reprovadas ou caixas).
    """
    for i in lista:
        if i[0] == id:
            print(f"[{i}] foi removida")
            lista.remove(i)
            return lista
    return False


def caixasFechadas(caixas):
    """
    Lista todas as caixas fechadas que já atingiram a capacidade máxima.
    """
    for c in caixas:
        print(c)


def relatorioFinal(aprovado, reprovado, caixas, caixa):
    """
    Gera o relatório consolidado de produção com os indicadores solicitados:
      - Total de peças aprovadas
      - Total de peças reprovadas
      - Total de caixas fechadas
      - Peças contidas na caixa em andamento
    """
    print(f"Total de peças aprovadas: {len(aprovado)}")
    print(f"Total de peças reprovadas: {len(reprovado)}")
    print(f"Total de caixas fechadas: {len(caixas)}")
    print(f"Caixa atual (em aberto): {caixa}")


# -----------------------------------------------------------------------------
# MENU INTERATIVO E FLUXO PRINCIPAL
# -----------------------------------------------------------------------------
while True:
    system('cls') 
    print('|-----------------------------------------------------------------------------------------------------------|')
    print('| [1] Nova peca  | [2] Aprovadas/reprovadas | [3] Remover peça | [4] Caixas | [5] Relatorio Final| [6] Sair |')
    print('|-----------------------------------------------------------------------------------------------------------|')
    opcao = input('')

    match opcao:
        # [1] Cadastrar nova peça
        case '1':
            system('cls')
            # 1. Identificação da peca que dever ser unica para permitir identificar peça para futura eliminação
            id = gerarid(listaIds)
            listaIds.append(id)  
            print(f"---- ID GERADO: {id} ----")

            # 2. Coleta de dados da peça
            peso = float(input('Qual o peso da peça? '))
            cor = input('Qual a cor da peça? [A] | [V] | [O-Outra]: ').strip().upper() #Independente se é digitado MAIUSCULO ou minusculo
            comprimento = float(input('Qual o comprimento da peça? '))
            motivo = ''

            # 3. peça criada e validadad
            peca = [id, peso, cor, comprimento, motivo]
            peca = validaPeca(peca)

            # 4. separação de peças APROVADAS ou REPROVADAS
            if peca[4] == '':
                # Peça APROVADA: Não tem motivo de reprovação pode ser armazenada
                if len(caixa) == 10:
                    caixas.append(caixa)  # Caixa aberta é armazenada 
                    caixa = []            # Caixa nova é aberta
                    aprovado.append(peca)
                    caixa.append(peca)    # Peca atual é adicionada na nova caixa
                else:
                    aprovado.append(peca)
                    caixa.append(peca)    # Peca atual é adicionada na caixa
            else:
                # Peça REPROVADA: é arquivada para controle de falahas com o motivo
                system('cls')
                reprovado.append(peca)
                print(f"Peça [{peca[0]}] foi REPROVADA!")
                print(f"Motivo(s): [{peca[4]}]")
                system('pause')

        # [2] Listar peças aprovadas/reprovadas
        case '2':
            system('cls')
            listaAprovadaReprovada(aprovado, reprovado)
            system('pause')

        # [3] Remover peça cadastrada
        case '3':
            system('cls')
            remover = int(input('Qual ID quer remover: '))
            # Procura e remove o ID em todos os locais onde ele pode estar registrado
            removePeca(aprovado, remover)
            removePeca(reprovado, remover)
            removePeca(caixa, remover)

            # Procura também dentro de cada uma das caixas já fechadas
            for c in caixas:
                removePeca(c, remover)
            system('pause')

        # [4] Listar caixas fechadas
        case '4':
            system('cls')
            caixasFechadas(caixas)
            system('pause')

        # [5] Gerar relatório final
        case '5':
            system('cls')
            relatorioFinal(aprovado, reprovado, caixas, caixa)
            system('pause')

        # [6] Sair
        case '6':
            system('cls')
            print("SAINDO DO SISTEMA")
            for i in range(5):
                print(".")
                time.sleep(1)
            break

        # Opção inválida
        case _:
            system('cls')
            print("Opcao invalida! Escolha uma opcao de 1 a 6.")
            system('pause')
