n1 = int(input('Digite um número'))
n2 = int(input('Digite outro número'))

s = n1 + n2
m = n1 * n2
p = n1 ** n2
dii = n1 // n2
di = n1 / n2
mod = n1 % n2
raiz = p ** (1/2)
print('Os números digitados foram {} e {} e a soma entre eles foi de {}'.format(n1,n2,s), end=' ')
print(',o produto entre eles é {} e a multiplicação entre eles é {}'.format(p,m))
print('A divisão entre eles é {:.3f},a divisão inteira entre eles é {} e o módulo entre eles é {}'.format(di,dii,mod))