from time import sleep
from random import randint
numeros = list()
numerosjogo = list()
n = int(input('Quantos jogos quer que eu sorteie?:'))
contador = 0
for i in range(0,n):
    for ii in range(0,6):
        numeros.append(randint(1,60))
        if len(numeros) == 6:
            break
    numerosjogo.append(numeros[:])
    numeros.clear()
print('-=-' * 5, f'Sorteando {n} jogos', '-=-' * 5)
for i,v in enumerate(numerosjogo):
    sleep(1)
    print(f'Jogo {i+1}: {v}')