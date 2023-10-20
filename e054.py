from datetime import date

ano = date.today().year
contador = 0
contadormenor = 0
for i in range(0,6):
    anonasc = int(input('Ano em que nasceu: '))
    idade = ano - anonasc
    if idade >= 21:
        contador += 1
    else:
        contadormenor += 1    
print ('{} pessoas entre as 6 já alcançaram a maioridade e {} ainda não'.format(contador,contadormenor))