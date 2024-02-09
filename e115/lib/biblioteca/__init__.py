def linha(tam=50):
    return '-' * tam


def cabecalho(txt):
    print(linha())
    print(txt.center(50))
    print(linha())

def menu(lista):
    cabecalho('Menu Principal')
    c = 1
    for item in lista:
        print(f'{c} - {item}')
        c += 1
    print(linha())
    opc = leiaInt('Sua opção:')
    return opc

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