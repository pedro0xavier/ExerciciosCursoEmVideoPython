
'''Desenvolva um programa que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status'''

peso = float(input('Qual o seu peso (Em KG): '))
altura = float(input('Qual a sua altura (Em Metros): '))
imc = peso / (altura * altura)
print ('O IMC dessa pessoa é {:.2F}'.format(imc))
if imc < 18.5:
    print('Abaixo do peso')
elif imc >= 18.5 and imc < 25:
    print ('Peso ideal')
elif imc >= 25 and imc < 30:
    print ('Sobrepeso')
elif imc >= 30 and imc < 40:
    print ("Obesidade")
else:
    print ('Obesidade mórbida')    
