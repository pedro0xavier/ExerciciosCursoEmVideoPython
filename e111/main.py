from utilidadesCeV import moeda
'''Crie um pacote chamado utilidadesCeV que tenha dois módulos internos chamados moeda e dado. Transfira todas as funções utilizadas nos desafios 107, 108 e 109 para o primeiro pacote e mantenha tudo funcionando'''
valor = float(input('Digite o preço: R$'))
Aumento = float(input('Taxa de aumento: '))
Reducao = float(input('Taxa de redução: '))
moeda.resumo(valor,Aumento,Reducao)