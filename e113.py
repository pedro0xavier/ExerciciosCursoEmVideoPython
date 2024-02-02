"""Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número de tipo inválido.Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.
"""


def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print("ERRO,Digite um número inteiro válido")
            continue
        except KeyboardInterrupt:
            print("Programa parado pelo teclado")
            return 0
        else:
            return n
            break

def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError,TypeError):
            print('ERRO,Digite um número real válido')
            continue
        except KeyboardInterrupt:
            print('Programa parado pelo teclado')
            return 0
        else:
            return n
            break
        
nn = leiaInt("Digite um número inteiro: ")
nnn = leiaFloat("Digite um número real")
print(f"O número inteiro digitado foi {nn} e o número real digitado foi {nnn}")