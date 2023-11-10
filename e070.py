'''Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:A) qual é o total gasto na compra.B) quantos produtos custam mais de R$1000.C) qual é o nome do produto mais barato.'''
maisde100 = contador = menor = total = 0
nomebarato = ''
while True:
    nome = 1
    nome = str(input('Nome do produto: '))
    preco = float(input('Preço do produto: R$'))
    contador+=1
    if contador == 1 or preco < menor:
        menor = preco
        nomebarato = nome
    if preco > 1000:
        maisde100+=1    
    total+=preco                
    respostas = ' '
    while respostas not in 'SsnN':
        respostas = str(input('Quer continuar? [S/N]')).upper().strip()[0]
        if respostas not in 'SN':
            print('Opção inválida digite S OU N ')
    if respostas == 'N':
        break
media = total / contador
print(f'O total gasto na compra foi de {total :.2f}')
print(f'A média dos {contador} produtos é {media :.2f}')
print(f'Há {maisde100} produtos que custam mais de R$1000 REAIS')
print(f'O produto mais barato é {nomebarato} que custa {menor :.2f}')
