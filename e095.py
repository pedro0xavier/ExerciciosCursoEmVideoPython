'''Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.'''
time = []
gols = list()
total = 0
while True:
    nome = str(input('Nome: '))
    games = int(input(f'Quantas partidas {nome} jogou?: '))
    for i in range(0,games):
        goles =  int(input(f'Quantos gols {nome} fez na partida {i + 1}?: '))
        gols.append(goles)
    time.append({'nome': nome, 'gols': gols.copy(), 'total': sum(gols), 'partidas': games})
    gols.clear()
    resp = str(input('Quer continuar?[S/N]:')).strip()[0]
    if resp in "nN":
        break
print('=-=' * 30)
print('{: <10}{: <10} {: <15}{: <15}'.format('N°','Nome', 'Gols', 'Total'))
print() 
for nO,dicionario in enumerate(time):
    print(f'{str(nO + 1):<10}{str(dicionario["nome"]):<10}{str(dicionario["gols"]):<15} {str(dicionario["total"]):<15}')
while True:
    n = int(input('Mostrar dados de qual jogador?: (999 para parar)'))
    n-=1
    if n + 1 == 999:
        break
    if n >= len(time) :
        print('Número inválido, digite um número válido consultando a tabela acima')
    elif n < 0:
        print('Número inválido, digite um número válido consultando a tabela acima')        
    else:
        print(f'    Mostrando dados do jogador {time[n]["nome"]}')
        for i in range(0,time[n]["partidas"]):
            print(f'Na partida {i+1} marcou {time[n]["gols"][i]} gols')