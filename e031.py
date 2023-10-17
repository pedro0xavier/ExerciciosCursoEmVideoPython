'''Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.'''
kmviagem = float(input('Qual é a distância da viagem? '))
print('Você está prestes a começar uma viagem de {:.1f}km'.format(kmviagem))
custoviagem = kmviagem * 0.45 if kmviagem <= 200 else kmviagem * 0.45
"""if kmviagem <= 200:
   custoviagem = kmviagem * 0.50
else:
    custoviagem = kmviagem * 0.45"""
print('E o preço dessa viagem será de R${:.2F}'.format(custoviagem))    