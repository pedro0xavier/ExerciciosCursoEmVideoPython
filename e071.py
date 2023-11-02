print ('-=-' * 30)
print ('{:^70}'.format('Banco'))
print ('-=-' * 30)
valor = int(input('Qual valor você quer sacar?'))
valor50 = valor // 50
valor20 = (valor % 50) // 20
valor10 = ((valor % 50)% 20) // 10
valor1 = valor % 10
print (f'Valor R${valor} ')
print (F'Em notas de 50: {valor50}')
print (F'Em notas de 20: {valor20}')
print (f'Em notas de 10: {valor10}')
print (f'Em notas de 1: {valor1}')

