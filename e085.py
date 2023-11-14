'''Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.
'''
numeros = [[],[]]
for i in range(0,6):
    n = int(input(f'Digite o número na posição {i}: '))
    if n % 2 == 0:
        numeros[0].append(n)
    else:
        numeros[1].append(n)

print(f'A lista completa: {numeros}')
print(f'A lista de pares: {sorted(numeros[0])}')
print(f'A lista de ímpares: {sorted(numeros[1])}')