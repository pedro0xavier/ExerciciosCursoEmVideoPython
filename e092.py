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