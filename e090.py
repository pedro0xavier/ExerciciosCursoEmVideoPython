''' Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.'''
pessoanota = {}
pessoanota["nome"] = str(input('Nome: '))
pessoanota ["media"] = float(input('Média: '))
if pessoanota["media"] >= 7:
    pessoanota["situacao"] = "Aprovado"
elif pessoanota["media"] >= 5 and pessoanota["media"] < 7:
    pessoanota["situacao"] = "Recuperação"
else:
    pessoanota["situacao"] = "Reprovado"
for x , y in pessoanota.items():
    print(f"O {x} é {y}")
