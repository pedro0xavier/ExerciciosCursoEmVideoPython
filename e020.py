''' O mesmo professor do desafio 019 quer sortear a ordem de apresentação de trabalhos dos alunos. 
Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.'''
from random import shuffle
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
n5 = str(input('Quinto aluno: '))

lista = [n1,n2,n3,n4,n5]

shuffle(lista)

print ('A nova ordem sorteada foi {}'.format(lista))

