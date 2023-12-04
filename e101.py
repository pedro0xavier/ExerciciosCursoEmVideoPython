'''Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.'''
import datetime as dt
ano = dt.date.today().year
idade = 0
def voto(anosnasc):
    global idade
    import datetime as dt
    ano = dt.date.today().year
    idade = ano - anosnasc
    if idade < 16:
        return 'Voto Negado'
    elif idade >= 16 and idade < 18:
        return 'Voto Opcional'
    else:
        return 'Voto Obrigatório'


datanasc = int(input("Em que ano você nasceu?: "))
votosituacao = voto(datanasc)
print(f'Idade {idade}: ')
print(f'Situação de voto: {votosituacao}')