'''Programa de aluguel de carros que pergunta os km percorridos e quantos dias ele foi alugado para calcular o valor a ser pago'''
a = 'ALUGEL DE CARROS'
print("{:^20}".format(a))

dias = float(input('Quantos dias rodados? '))
kmpcr = float(input('KM percorridos? '))
valor = (60*dias) + (0.15*kmpcr)

print('O total a pagar é R${:.2f}'.format(valor))