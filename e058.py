'''Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10.
 Só que agora o jogador vai tentar adivinhar até acertar, ]
 mostrando no final quantos palpites foram necessários para vencer.'''
from random import randint
print('-=-' * 30)
txt = 'Vou pensar em um número de 0 a 5. Tente adivinhar.......'
x = txt.center(20)
print(x)
print('-=-' * 30)
controle = False
tentativas = 0
computador = randint(0,5)
while not controle:
    jogador = int(input('Em que número pensei? '))
    if computador != jogador:
        print('Tente novamente')
        tentativas += 1
        if jogador < computador:
            print('O número é maior')
        if jogador > computador:
            print('O número é menor')
    else:
        print('Você ganhou, esse foi o número que eu pensei')
        controle = True
        print('Foram necessarias {} tentativas para acertar o número'.format(tentativas))
