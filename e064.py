'''Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).'''
num = 0
contagem = 0 
soma = 0
num = int(input('Digite um número [999] para parar: '))
while num != 999:
    contagem +=1
    soma += num
    num = int(input('Digite um número [999] para parar: '))
print (f'Soma dos números digitados é {soma} e foram digitados {contagem} números')