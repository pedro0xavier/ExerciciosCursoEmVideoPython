# Um programa para aprovação de um empréstimo bancário para a compra de uma casa, perguntando o valor de uma casa, o sálario do comprador e em quantos anos ele irá pagar

valorcasa = float(input('Valor da casa :R$'))
salario = float(input ('Salário do comprador em R$: '))
anos = float(input ('Em quantos anos ele vai pagar: ')) # Pensei em botar como int mas ele pode querer pagar em 4 anos e meio 

meses = anos * 12
prestacao = valorcasa / meses # Eu sei que é meio inútil fazer essa variável pois eu podeira fazer anos * 12 direto  
minimo = (salario * 30) / 100 
print ('Para pagar uma casa de {:.2F} em {:.2F} terá uma prestação mensal de R${:.2F}'.format(valorcasa,anos,prestacao))
if prestacao <= minimo:
 print ("Empréstimo permitido!!!!")
else:
 print ('Empréstimo negado!!!!!')