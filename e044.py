'''Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento'''
preco = float(input('Preço do produto: R$'))
print('FORMAS DE PAGAMENTO ')
print ('[1] à vista dinheiro ou cheque')
print ('[2] à vista cartão')
print ('[3] 2x no cartão')
print ('[4] 3X ou mais no cartão')

opcao = int(input('Qual a opção?'))
match opcao:
    case 1:
        total = preco - (preco * 10 / 100)
    case 2:
        total = preco - (preco * 5 / 100)
    case 3: 
        print ('Sua parcela ficará {} parcelas de {:.3f}'.format(2,preco))
    case 4:
        parcelas = int(input('Será feitas em quantas parcelas '))
        preco = preco + (preco * 20 / 100)
        print ('Sua parcela ficará {}x de {:.2f} com juros'.format(parcelas,preco / parcelas))
    case other:
        preco = 0
        print ('A opção digitada não é válida')   
print ('Sua compra ficará ao total {:.2f}'.format(preco))    