from datetime import date
print ('Serviço de checagem do alistamento militar')
ano = int(input('Ano de nascimento: '))
anoatual = date.today().year
idade = anoatual - ano

print ('Quem nasceu em {} tem {} anos em {}'.format(ano,idade,anoatual))

if idade < 18:
    saldo = 18 - idade # tempo restante até o alistamento
    print ('Ainda faltam {} anos para o alistamento'.format(saldo))
    print ('Seu alistamento será em {}'.format(anoatual + saldo))
elif idade > 18:
    saldo = idade - 18 # quanto tempo já passou do seu prazo de alistamento
    print ('Já se passaram {} anos do seu alistamento '.format(saldo))
    print ('Seu alistamento foi em {}'.format(anoatual - saldo))
elif idade == 18:
    print ('Sua hora de se alistar chegou!!!!!')    