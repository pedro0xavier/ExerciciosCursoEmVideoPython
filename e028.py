'''Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu'''
from random import randint
from time import sleep
print('-=-' * 30)
txt = 'Vou pensar em um número de 0 a 5. Tente adivinhar.......'
x = txt.center(20)
print (x)
print('-=-' * 30)

computador = randint(0,5)
jogador = int(input('Em que número pensei? '))
print ('Processando........')
sleep(2.5)
if computador == jogador:
    print ('Você ganhou, esse foi o número que eu pensei')
else:
    print('EU GANHEI!!!!!!!, pensei no número {} e você pensou no número {}'.format(computador,jogador))