'''Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular e outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.'''
def ficha(name = 'Desconhecido',goles = 0):
    return f'O jogador {name} marcou {goles} gol(s) no campeonato'

print('-=-' * 30)
nome = str(input('Nome do jogador: ')).strip()
gols = str(input('Quantos gols o jogador fez no campeonato?: '))
if gols.isnumeric():
    gols  = int(gols)
else:
    gols = 0
if nome == '':
    print(ficha(goles=gols))
else:
    print(ficha(gols,nome))