cont = 1
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
pa = primeiro
termo = 10
total = 0
while termo != 0:
    total += termo
    while cont <=total:
        print('{} ->'.format(pa), end=' ')
        pa+=razao
        cont +=1
    print ('fim')
    
    termo = int(input('Quantos termos você quer ver a mais?'))
print (f'Progressão finalizada com  {total} termos mostrados')