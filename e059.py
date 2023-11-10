'''Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar,[ 2 ] multiplicar,[ 3 ] maior,[ 4 ] novos números,[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.'''
from time import sleep
n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número:'))
opcao = 0
while opcao != 5:
    sleep(1)
    print('Escolha uma das opções')
    print('[1] somar')
    print('[2] multiplicar')
    print('[3] maior')
    print('[4] novos números')
    print('[5] Sair')
    opcao = int(input('Qual vai ser a opção escolhida?: '))
    match opcao:
        case 1:
            print ('A soma entre {} e {} é {}'.format(n1,n2,n1 + n2))
        case 2:
            print('O resultado da multiplicação entre {} e {} é {}'.format(n1,n2,n1 * n2))
        case 3:
            if n1 > n2:
                maior = n1
                print ('O maior número entre os dois é {}'.format(maior))
                print ('O maior número entre {} e {} é {}'.format(n1,n2,maior))
            elif n2 > n1:
                maior = n2
                print ('O maior número entre {} e {} é {}'.format(n1,n2,maior))
            else:
                print('Não há um número maior entre os dois pois ambos são iguais')
        case 4:
            n1 = int(input('Qual é o primeiro número: '))
            n2 = int(input('Qual é o segundo número: '))
        case 5:
            print ('Até mais.....')
        case other:
            print ('Opção inválida, insira outra opção')
    print ('===' * 30)                   
