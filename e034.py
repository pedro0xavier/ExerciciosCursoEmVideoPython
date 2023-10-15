salario = float(input('Digite o salário para calcular o aumento '))
if salario > 1250.0:
    nsalario = salario + ((salario * 10) / 100)
else:
    nsalario = salario + (salario * 15 / 100)  
print ('Quem ganhava R${:.2f} após o aumento recebe um salário de R${:.2f}'.format(salario,nsalario))     