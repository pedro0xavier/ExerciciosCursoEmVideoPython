#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input('Digite o salário para calcular o aumento '))
if salario > 1250.0:
    nsalario = salario + ((salario * 10) / 100)
else:
    nsalario = salario + (salario * 15 / 100)  
print ('Quem ganhava R${:.2f} após o aumento recebe um salário de R${:.2f}'.format(salario,nsalario))     