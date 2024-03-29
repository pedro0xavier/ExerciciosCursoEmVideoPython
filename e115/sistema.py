from lib.biblioteca import *
from lib.arquivos import *

arq = "arquivo.txt"
if existeArquivo(arq):
    print("Arquivo Encontrado com sucesso")
else:
    print("Arquivo não encontrado")
    criararquivo(arq)
while True:
    resposta = menu(
        ["Ver Pessoas Cadastradas", "Cadastrar Novas Pessoas", "Sair do Sistema"]
    )
    match resposta:
        case 1:
            cabecalho("VER PESSOAS CADASTRADAS:")
            lerArquivo(arq)
        case 2:
            cabecalho("CADASTRAR PESSOAS:")
            aa = str(input('Digite o nome que quer cadastrar no sistema: '))
            idade = int(input('Digite a idade da pessoa cadastrada: '))
            escreverArquivo(arq,aa,idade)
        case 3:
            cabecalho("Encerrando o programa.....")
            break
