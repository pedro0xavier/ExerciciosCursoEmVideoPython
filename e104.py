'''Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante a função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico. Ex: n = leiaInt(Digite um n: )'''
def leiaint(mensagem):
    n = str(input(mensagem)).strip()
    if n.isnumeric() == True:
        int(n)
    if n.isnumeric() == False or n == '':
        return 'ERRO, DIGITE UM NÚMERO'
    else:
        return f'O número digitado foi {n}'
nn = leiaint('Digite um número: ')
print(nn)