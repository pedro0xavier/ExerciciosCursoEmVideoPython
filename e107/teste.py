from moeda import * 
'''Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade(). Faça também um programa que importe esse módulo e use algumas dessas funções.'''
print(f'O valor com 20% de juros é {aumentar(300.50,20)}')
print(f'O valor com 20% de desconto é {diminuir(300.50,20)}')
print(f'O dobro do valor é {dobro(300.50)}')
print(f'O triplo do valor é {triplo(300.50)}')