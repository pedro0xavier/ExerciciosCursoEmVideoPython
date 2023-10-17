#Programa que recebe o valor do cateto oposto e adjacente para calcular o comprimento da hipotenusa
from math import hypot
print ('Cálculo de hipotenusa')
n = float(input('Digite o cateto adjacente '))
nn = float(input('Digite o cateto oposto '))
print ('O cateto da hipotenusa tem o valor de {:.2f}'.format(hypot(n,nn)))