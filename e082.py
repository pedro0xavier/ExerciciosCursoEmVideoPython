'''Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.
'''
numeros = list()
while True:
    numeros.append(int(input('Digite um número: ')))
    resp = str(input('Quer continuar?[S/N]: ')).strip().upper()[0]
    if resp in 'nN':
        break
pares = list()
impares = list()
for n in numeros:
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
print(f'A lista completa é {numeros}')
print(f'A lista de pares é {pares}')
print(f'A lista de ímpares é {impares}')