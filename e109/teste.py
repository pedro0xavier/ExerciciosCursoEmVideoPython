from moeda import * 
'''Adapte o código do desafio #107, criando uma função adicional chamada moeda() que consiga mostrar os números como um valor monetário formatado.'''
valor = float(input('Digite o preço: R$'))
print(f'R${valor} com 20% de juros é {aumentar(valor,20,True)}')
print(f'O R${valor} com 20% de desconto é {diminuir(valor,20,True)}')
print(f'O dobro de R${valor} é {dobro(valor,True)}')
print(f'O triplo de R${valor} é {triplo(valor)}')