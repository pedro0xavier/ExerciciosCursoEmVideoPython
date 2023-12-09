from moeda import * 
'''Modifique as funções que form criadas no desafio 107 para que elas aceitem um parâmetro a mais, informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.
'''
valor = float(input('Digite o preço: R$'))
print(f'R${valor} com 20% de juros é {aumentar(valor,20,True)}')
print(f'O R${valor} com 20% de desconto é {diminuir(valor,20,True)}')
print(f'O dobro de R${valor} é {dobro(valor,True)}')
print(f'O triplo de R${valor} é {triplo(valor)}')