from utilidadesCeV import moeda
from utilidadesCeV import dado
'''Crie um pacote chamado utilidadesCeV que tenha dois módulos internos chamados moeda e dado. Transfira todas as funções utilizadas nos desafios 107, 108 e 109 para o primeiro pacote e mantenha tudo funcionando'''
valor = dado.leiadinheiro('Preço: ')
Aumento = dado.leiadinheiro('Taxa de Aumento: ')
Reducao = dado.leiadinheiro('Taxa de Diminuindo: ')
moeda.resumo(valor,Aumento,Reducao)