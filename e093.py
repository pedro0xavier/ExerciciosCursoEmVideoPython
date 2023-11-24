dados = {}
gols = list()
nome= dados['Nome'] = str(input('Nome do jogador: ')).strip().title()
games = int(input('Quantas partidas jogou?: '))
total = 0
for i in range(0,games):
    gols.append(int(input(f'Quantos gols {nome} fez na partida {i + 1}: ')))
    total = gols[i] + total
dados['Gols'] = gols.copy()
dados['Total de gols'] = total
print('-=-' * 30)
print (dados)
print('-=-' * 30)
for keyy,itemm in dados.items():
    print(f'{keyy} é {itemm}')
print('O jogador {} jogou {} jogos '.format(dados['Nome'],games))
for i in range (0,games):
    print(f'Na partida {i + 1} marcou {gols[i]} gols')
print(f'Foi um total de {total} gols')
print(f'A partida que mais marcou gols foi na {gols.index(max(gols)) + 1}° onde marcou {max(gols)} gols')
print(f'A partida que menos marcou gols foi na {gols.index(min(gols)) + 1}° onde marcou {min(gols)} gols')