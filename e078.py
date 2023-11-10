'''Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.'''
lista = []
for i in range(0,5):
    lista.append(int(input(f'Digite um número para a posição {i}: ')))
print (f'Os números digitados foram {lista}')
valormax = max(lista)
valormin = min(lista)
maxindex = [i for i in range(len(lista)) if lista[i] == valormax]
minindex = [cont for cont in range(len(lista)) if lista[cont] == valormin]
print (f'O maior valor foi {valormax} ',end='')
if len(maxindex) > 1:
    print('e os valores apareceram nas posições',end = '')
    for mi in maxindex:
        print(end=''f' {mi}')
else:
    print ('e o valor apareceu na posição ',end='')
    for mi in maxindex:
        print(f'{mi}',end='')
print('\r')           
print (f'O menor valor foi {valormin} ', end='')
if len(minindex) > 1:
    print('e os valores apareceram nas posições',end='')
    for min in minindex:
        print(end=''f' {min}')
else:
    print('e o valor apareceu na posição ',end='')
    for min in minindex:
        print (f'{min}')                    