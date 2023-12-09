from moeda import * 
'''Adapte o código do desafio #107, criando uma função adicional chamada moeda() que consiga mostrar os números como um valor monetário formatado.'''
valor = float(input('Digite o preço: R$'))
print(f'R${valor} com 20% de juros é {moeda(aumentar(valor,20))}')
print(f'O R${valor} com 20% de desconto é {moeda(diminuir(valor,20))}')
print(f'O dobro de R${valor} é {moeda(dobro(valor))}')
print(f'O triplo do R${valor} é {moeda(triplo(valor))}')