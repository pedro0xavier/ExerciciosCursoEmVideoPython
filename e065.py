'''Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.'''
cont ='S'
menor = maior = contagem = media = soma = 0
while cont in 'sS':
    num = int(input('Digite um número: '))
    if cont != 'S':
        break
    soma += num
    contagem += 1
    if contagem == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    media = soma / contagem
    cont = str(input('Quer continuar? [S/N]')).upper().strip()[0]
print(f'Você digitou {contagem} números e tem a média de {media}')
print(f'O maior número digitado foi {maior} e o menor número digitado foi {menor}')