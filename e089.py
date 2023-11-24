'''Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.'''
dados = list()

while True:
    nome = str(input('Nome: ').title()) 
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    media = (n1 + n2) / 2
    dados.append([nome, [n1, n2], media])
    
    resp = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break

print('=-=' * 15)
print(f'{"No.": <4}{"Nome": <10}{"Média": >8}')
print('-' * 30)

for i, aluno in enumerate(dados, 1):
    print(f'{i:<4}{aluno[0]:<10}{aluno[2]:>8.1f}')

while True:
    index = int(input('\nMostrar a nota de qual aluno (baseado no número da chamada) [Digite 999 para sair]: ')) - 1

    if index == 999:
        break

    print(f'\nNotas do(a) {dados[index][0]}: {dados[index][1]}')
