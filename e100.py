"""Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.
"""
from time import sleep
from random import randint
lista = []
soma = []
def sorteia():
    for i in range(0,5):
        lista.append(randint(1,11))
sorteia()
def somapar():
    print("Os números sorteados foram: ",end='')
    for numero in lista:
        print(numero,end=' ', flush=True)
        sleep(1)
        if numero % 2 == 0:
            soma.append(numero)
    print()
    print(f"A soma da lista {lista} foi {sum(soma)}")
somapar() 
