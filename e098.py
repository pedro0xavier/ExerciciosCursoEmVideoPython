'''
faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo. Seu programa tem que realizar três contagens através da função criada:a) de 1 até 10, de 1 em 1
b) de 10 até 0, de 2 em 2
c) uma contagem personalizada
'''
from time import sleep
def contador(inicio,fim,passo):
    print('-=-'* 30)
    print('Contador de 1 a 10 de 2 em 2')
    for i in range(1,11):
        print(i,end = ' ')
        sleep(1)
    print()
    print('-=-'* 30)
    print('Contador de 10 a 0 de 2 em 2')
    for i in range(10,-1,-2):
        print(i,end=' ')
        sleep(1)
    print()
    print('-=-'* 30)
    print('Agora é a sua vez de realizar a contagem')
    inicio = int(input('Inicio: '))
    fim = int(input('Fim: '))
    passo = int(input('Passo: '))
    for i in range(inicio,fim,passo):
        print(i)
contador(inicio = 1,fim = 3,passo = 1) 