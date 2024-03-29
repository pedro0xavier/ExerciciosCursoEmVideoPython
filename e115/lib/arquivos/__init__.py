from lib.biblioteca import *


def existeArquivo(name):
    try:
        a = open(name, "rt", encoding="utf-8")
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criararquivo(name):
    try:
        a = open(name, "wt+", encoding="utf-8")
        a.close()
    except:
        print("OCORREU UM ERRO TENTE NOVAMENTE MAIS TARDE")
    else:
        print(f"O arquivo {a} foi criado com sucesso")


def lerArquivo(name):
    try:
        arquivo = open(name, "r")
    except:
        print("OCORREU UM ERRO, TENTE EM OUTRO MOMENTO")
    else:
        cabecalho("PESSOAS CADASTRADAS")
        print(arquivo.read())
        '''for linha in arquivo:
            dado = linha[:-1].split(",")
            print(f"{dado[0]:<30}{dado[1]:>3} anos")'''
    finally:
        arquivo.close()


def escreverArquivo(arquivo, nome="Desconhecido", idade=0):
    try:
        arquivo = open(arquivo, "at", encoding="utf-8")
    except:
        print("UM ERRO ACONTECEU,TENTE EM OUTRO MOMENTO")
    else:
        try:
            arquivo.write(f"\n{nome},{idade} anos")
        except:
            print("Houve um erro ao tentar adicionar o arquivo")
        else:
            print(
                "Nome e idade foram adicionados com sucesso foram adicionados com sucesso"
            )
            arquivo.close()
