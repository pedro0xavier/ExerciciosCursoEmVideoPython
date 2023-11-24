'''Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.'''
from datetime import datetime
dados = {}
dados['Nome'] = str(input('Nome: ')).title()
anonasc = int(input('Ano de nascimento: '))
dados['Idade'] = datetime.now().year - anonasc
dados['CLT'] = int(input('Carteira de trabalho(0 se não tiver): '))
if dados['CLT'] != 0:
    dados['Ano contratação'] = int(input('Ano de contratação: '))
    dados['Salário'] = float(input('Salário: '))
    dados['Aposentadoria'] = dados['Idade'] + ((dados['Ano contratação'] + 35) - datetime.now().year)
print('-=-'*30)
for keyy, itemm in dados.items():
    print(f'{keyy} é {itemm}')