#Programa que leia o salário de um funcionário e depois o mostre com o aumento de 15%
salario = float(input('Digite o seu salário para receber o aumento R$'))
aumento = salario + (salario * 15 / 100)

print ('Seu salário que era de R${} após o aumento de 15% ficou com o valor de R${:.2f} '.format(salario,aumento))