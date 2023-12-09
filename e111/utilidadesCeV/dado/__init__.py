'''Dentro do pacote utilidadesCeV que criamos no desafio 111, temos um módulo chamado dado. Crie uma função chamada leiaDinheiro() que seja capaz de funcionar como a função imputa(), mas com uma validação de dados para aceitar apenas valores que seja monetários.'''
def is_number(string):
    try:
        float(string)
        return True
    except ValueError:
        return False

def leiadinheiro(msg):
    valido = False
    while not valido:
        entrada =str(input(msg)).replace(',','.').strip()
        if entrada.isnumeric() or is_number(entrada) == True or entrada != '':
            valido = True
            return float(entrada)
        else:
            print(f'ERRO {entrada} é um número inválido')