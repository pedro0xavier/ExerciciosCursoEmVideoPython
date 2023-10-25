n1  = int(input('Digite um número para vermos seu fatorial: '))
c = n1
fat = 1
print ('Calculando {}! = '.format(n1),end= '')
while c > 0:
    print ('{} '.format(c), end = '')
    print ('x ' if c > 1 else '= ',end = '')
    fat*=c
    c-=1
print('{}'.format(fat)) 

