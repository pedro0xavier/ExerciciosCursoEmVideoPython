'''Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.'''
dados = list()
pessoa = list()
media = list()
while True:
    dados.append(str(input('Nome:' )))
    dados.append(float(input(f'Nota 1: ')))
    dados.append(float(input(f'Nota 2: ')))
    for i in range(0,2):
        media.append(dados[i][:])
        
    pessoa.append(dados[:])
    dados.clear()
    resp = str(input('Quer continuar?: [S/N]')).strip().upper()[0]
    if resp in 'N':
        break
print('=-='*30)
print(f'No.',end=' ')
print('Nome',end='')
print(f'{"Média": >20}')
for i in range(len(pessoa)):
    print(i,end='  ')
    print(f'{pessoa[i][0]}',end='  ')
    print()
