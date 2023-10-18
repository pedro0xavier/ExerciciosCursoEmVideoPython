from random import randint
from time import sleep 
# Fazer um programa para jogar pedra,papel, tesoura com a máquina 

print ('JOKENPO')
print ('Escolha entre as opções abaixo')
print ( 'PEDRA') 
print ('PAPEL')  
print ('TESOURA') 

option = str(input('Digite a sua escolha: '))
print ('JO')
sleep(1)
print ('KEN')
sleep(1)
print('PO')
opcao = option.title()
escolha = randint(0,2)
actioncomp = ['Pedra','Papel','Tesoura'] # Poderia ter usado choice mas achei mais prático me basear pelo index 
match opcao: # Usei o match case ao invés de diversos elif por deixar o código mais limpo 
    case 'Tesoura':
        if escolha == 0:
            print ('Você perdeu pois escolheu {} e máquina escolheu {}'.format(opcao,actioncomp[escolha])) 
        elif escolha == 1:
            print ('Você ganhou pois escolheu {} e a máquina escolheu {}'.format(opcao,actioncomp[escolha]))
        else:
            print ('Você empatou com a máquina pois ambois escolheram {}'.format(opcao))
    case 'Papel':             
        if escolha == 0 :
            print ('Você ganhou pois escolheu {} e a máquina escolheu {}'.format(opcao,actioncomp[escolha]))
        elif escolha == 2:
            print ('Você perdeu pois escolheu {} e máquina escolheu {}'.format(opcao,actioncomp[escolha])) 
        else:
            print ('Você empatou com a máquina pois ambois escolheram {}'.format(opcao))
    case 'Pedra':
        if escolha == 1:
            print ('Você perdeu pois escolheu {} e máquina escolheu {}'.format(opcao,actioncomp[escolha]))
        elif escolha == 2:
            print ('Você ganhou pois escolheu {} e a máquina escolheu {}'.format(opcao,actioncomp[escolha]))
        else:
            print ('Você empatou com a máquina pois ambois escolheram {}'.format(opcao))
    case other:
            print ('A opção escolhida não é válida, tente novamente')

