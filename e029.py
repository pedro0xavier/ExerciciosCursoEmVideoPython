velocidade = float(input('Qual a velocidade atual do carro? '))
if velocidade > 80.0:
    print('MULTADO!!! Você excedeu o limite de velocidade de 80Km/h')
    multa = (velocidade - 80) * 7.00
    print ('Você deve pagar uma multa de R${:.2f}'.format(multa))
print ('Tenha um bom dia e dirija em segurança')
