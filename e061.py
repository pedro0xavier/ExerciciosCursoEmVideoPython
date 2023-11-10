'''Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.'''
cont = 1
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
pa = primeiro
while cont <=10:
    print('{} ->'.format(pa), end=' ')
    pa+=razao
    cont +=1
print ('fim')
