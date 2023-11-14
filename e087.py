''' Aprimore o desafio anterior, mostrando no final:A) A soma de todos os valores pares digitados.B) A soma dos valores da terceira coluna.C) O maior valor da segunda linha.'''
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
soma = matriz[0][2] + matriz[1][2] + matriz[2][2]
for m in range(0,3):
    if m == 0:
        maior = matriz[1][m]
    elif maior < matriz[1][m]:
        maior = matriz[1][m]
somapar = 0
for linha in range(0,3):
    for coluna in range(0,3):
        if matriz[linha][coluna] % 2 == 0:
            somapar +=matriz[linha][coluna]
print()
print(f'A soma dos valores da terceira coluna: {soma} ')
print(f'A soma dos valores pares é: {somapar} ')
print(f'O maior valor da segunda coluna é : {maior} ')