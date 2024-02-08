'''Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai aparecer. Quando o usuário digitar a palavra FIM , o programa se encerrará. Importante: use cores.'''
def ajuda(ajuuda):
    print('-=-'* 30)
    print(f'Acessando o comando {ajuuda}')
    print('-=-' * 30)
    help(ajuuda)


def titulo(ajuuda):
    tam = len(ajuuda)
    print('-=-' * tam)
    print(ajuuda)
    print('-=-' * tam)


while True:
    titulo("SISTEMA DE AJUDA PYHELP")
    comando = str(input('Digite a função ou biblioteca: ')).strip()
    if comando.upper() == 'FIM':
        print('ATÉ LOGO')
        break
    help(comando)
titulo("Até logo")
