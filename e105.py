'''Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:
– Quantidade de notas
– A maior nota
– A menor nota
– A média da turma
– A situação (opcional)'''
def notas(*notas,sit):
    notaturma = {}
    notaturma["Maior"] = max(notas)
    notaturma["Menor"] = min(notas)
    notaturma["Total"] = len(notas)
    notaturma["Média"] = round(sum(notas) / len(notas),2)
    if sit:
        if notaturma["Média"] < 6:
            notaturma["Situação"] = "Ruim"
        else:
            notaturma["Situação"] = "Boa"
    return notaturma
print(notas(5.5,7.8,1.3,9.3,sit=True))
print(notas(5.5,7.8,1.3,3.3,sit=True))
print(notas(5.5,7.8,7.3,9.3,sit=True))
