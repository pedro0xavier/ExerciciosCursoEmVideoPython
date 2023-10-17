# Programa que recebe um ângulo e diz o valor do seno,cosseno e tangente
from math import radians,cos,sin,tan
an = float(input("Digite o ângulo que quer saber os valores "))
ii= radians(an)
x1 = cos(ii)
x2 = sin(ii)
x3 = tan(ii)

print('O ângulo de {} tem o valor do cosseno de {:.2f}'.format(an,x1), end = '')
print('o ângulo de {} tem o valor do seno de {:.2f}'.format(an,x2),end = '')
print ('o ângulo de {} tem o valor da tangente de {:.2f}'.format(an,x3))