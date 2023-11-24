'''Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.'''
dados = {}
gols = list()
dados['Nome'] = str(input('Nome do jogador: ')).strip().title()
games = int(input(f'Quantas partidas {dados["Nome"]} jogou?: '))
total = 0
for i in range(0,games):
    gols.append(int(input(f'Quantos gols {dados["Nome"]} fez na partida {i + 1}: ')))
dados['Gols'] = gols.copy()
dados['Total'] = sum(gols)
print('-=-' * 30)
print (dados)
print('-=-' * 30)
for keyy,itemm in dados.items():
    print(f'{keyy} é {itemm}')
print('-=-' * 30)
print(f'O jogador {dados["Nome"]} jogou {games} jogos ')
for i,g in enumerate(dados['Gols']):
    print(f'Na partida {i + 1} marcou {g} gols')
print(f'Foi um total de {dados["Total"]} gols')
print(f'A partida que mais marcou gols foi na {gols.index(max(gols)) + 1}° onde marcou {max(gols)} gols')
print(f'A partida que menos marcou gols foi na {gols.index(min(gols)) + 1}° onde marcou {min(gols)} gols')