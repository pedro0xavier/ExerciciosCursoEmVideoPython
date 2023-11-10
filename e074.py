'''Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.'''
from random import randint

tupla = ('','','','')
mylist = list(tupla)
for i in range(0,4):
    numrand = randint(1,10)
    mylist[i] = numrand
    if i == 0:
        maior = mylist[i]
        menor = mylist[i]        
    if mylist[i] > maior:
        maior = mylist[i]
        posmaior = i
    if mylist[i] < menor:
        menor = mylist[i]
        posmenor = i    
print(tuple(mylist))
print(f'O maior número é {maior} que está na posição {posmaior}')
print(f'O menor número é {menor} que está na posição {posmenor}')
