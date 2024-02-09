from lib.biblioteca import *
while True:
    resposta = menu(['Ver Pessoas Cadastradas' , 'Cadastrar Novas Pessoas' ,'Sair do Sistema'])
    match resposta:
        case 1:
            cabecalho('VER PESSOAS CADASTRADAS:')
        case 2:
            cabecalho('Cadastrar novas pessoas:')
        case 3:
            cabecalho('Encerrando o programa.....')
            break