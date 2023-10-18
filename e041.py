'''A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade'''
from datetime import date
anonasc = int(input('Ano de nascimento: '))
ano = date.today().year
idade = ano - anonasc
print ('O atleta tem {} anos '.format(idade))

if idade <= 9:
      print ('Classificação: MIRIM')
elif idade <= 14: 
    print ('Classificação: INFANTIL')
elif idade <= 19:
    print ('Classificação: JUNIOR')
elif idade <= 25:
    print ('Classificação: Sênior')
else:
    print ('Classificação: MASTER')

