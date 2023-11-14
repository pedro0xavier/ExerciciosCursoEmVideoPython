'''Crie um programa que declare uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta.'''
matriz = list()
for i in range (0,3):
    numeros = list() 
    for ii in range (0,3):
        numeros.append(int(input(f'Digite o número para a posição {i},{ii}: ')))    
    matriz.append(numeros)
for i in range(0,3):
    print()
    for ii in range(0,3):
        print(f'[{matriz[i][ii]:^3}]', end='')
print()


