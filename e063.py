'''Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci.'''
print('=-=' * 30)
print('Seqûencia de fibonnaci')
print('=-=' * 30)
n1 = 0
termos = int(input('Quuantos termos quer mostrar? '))
cont = 0
n2 = 1
while cont <= termos:
    print (f'{n1} -', end=' ')
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    cont+=1
print ("Fim")    