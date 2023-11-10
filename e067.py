'''Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.'''
while True:
    n = int(input('Digite qual tabuada quer ver '))
    if n < 0:
        break
    contador = 0
    for contador in range (1,11):
        print (f'{n} x {contador} = {n * contador}')
        contador+=1
print ('Até mais.....')
