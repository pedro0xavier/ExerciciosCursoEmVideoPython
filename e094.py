''' Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: A) Quantas pessoas foram cadastradas B) A média de idade C) Uma lista com as mulheres D) Uma lista de pessoas com idade acima da média'''
pessoas = []
mulheres = []
while True:
    nome = str(input('Nome:').strip().title())
    idade = int(input('Idade:'))
    sexo = str(input('Sexo[M/F]:').strip().upper()[0])
    if sexo not in "mMFf":
        print('ERRO DIGITE M OU F')
        sexo = str(input('Sexo[M/F]:').strip().upper()[0])
    pessoas.append({'Nome':nome,'Idade': idade, 'Sexo':sexo})
    resp = str(input('Quer continuar?[S/N]:'))
    if sexo in 'F':
        mulheres.append({'Nome': nome})
    if resp in "nN":
        break
mlist = [m['Nome'] for m in mulheres]
media = sum(item['Idade'] for item in pessoas) / len(pessoas)
print(f'Ao todo foram cadastadas {len(pessoas)} pessoas')
print (f'A média de idade é {media :.2f}')
print (f'As mulheres da lista são ',end='')
for p in pessoas:
   if p['Sexo'] == 'F':
       print (f'{p["Nome"]} ',end=' ')