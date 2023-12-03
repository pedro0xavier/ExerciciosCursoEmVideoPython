''' Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.'''
from time import sleep
def maior(*num):
    bigger = max(num,key=int)
    print(f'Foram printados os números:',end=' ')
    for numeros in num:
        print(f'{numeros}',end=' ')
        sleep(1)
    print()
    print(f'Ao todo foram digitados {len(num)} números ')
    print(f'O maior número digitado foi {bigger}')
    print('-=-'*30)
maior(5,4,8,9,3)
maior(9,8,7,6,19,44,83)