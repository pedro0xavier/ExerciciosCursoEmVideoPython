#Algoritmo que leia o preço de um produto e depois o mostre com um desconto de 5%
valor = float(input("Digite um valor R$"))

desconto = valor-(valor * 5 / 100)

print ("O produto que custava R${} com 5% de desconto agora custa R${}".format(valor,desconto))