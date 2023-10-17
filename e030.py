#Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
num = int(input('Fale um número '))
if num % 2 == 0:
    print('O número {:.1f} é par '.format(num))
else:
    print ('O número {:.1f} é ímpar'.format(num))
