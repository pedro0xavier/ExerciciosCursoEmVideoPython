def ficha(name = 'Desconhecido',goles = 0):
    return f'O jogador {name} marcou {goles} gol(s) no campeonato'

print('-=-' * 30)
nome = str(input('Nome do jogador: ')).strip()
gols = str(input('Quantos gols o jogador fez no campeonato?: '))
if gols.isnumeric():
    gols  = int(gols)
else:
    gols = 0
print(ficha(nome,gols))