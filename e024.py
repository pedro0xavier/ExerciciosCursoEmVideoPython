#Um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".
city = str(input('Informe a sua cidade ')).strip()
print(city[:5].upper() == 'SANTO')
