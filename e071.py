print ('-=-' * 30)
print ('{:^70}'.format('Banco'))
print ('-=-' * 30)
valor = int(input('Qual valor você quer sacar?: '))
valor100 = valor // 100
valor50 = valor % 100 // 50
valor20 = (valor % 50) // 20
valor10 = ((valor % 50)% 20) // 10
valor1 = valor % 10
print (f'Valor R${valor} ')
if valor100 > 0 or valor100 > valor:
    print (f'Em notas de 100: {valor100}')
if valor50 > 0:
    print (F'Em notas de 50: {valor50}')
if valor20 > 0:
    print (F'Em notas de 20: {valor20}')
if valor10 > 0:
    print (f'Em notas de 10: {valor10}')
if valor1 > 0:
    print (f'Em notas de 1: {valor1}')

