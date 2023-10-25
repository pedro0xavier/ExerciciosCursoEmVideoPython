cont = 1
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
pa = primeiro
while cont <=10:
    print('{} ->'.format(pa), end=' ')
    pa+=razao
    if cont == 10:
        print ('fim')
    cont +=1