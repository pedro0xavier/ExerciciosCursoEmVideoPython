from random import randint
print ('-=-' * 30)
print ('PAR OU ÍMPAR')
print ('-=-' * 30)
cont = 0
while True:
    valorcomp = randint(0,10)
    valor = int(input('Digite um valor '))
    print ('O programa para quando perder')
    total = valor + valorcomp
    imparpar = ' '
    while not imparpar in 'PI':
        imparpar = str(input('PAR OU ÍMPAR [P/I]')).upper().strip()[0]
        print(f'Você jogou {valor} e computador jogou {valorcomp} e deu {total}')
        print ('Deu par' if total % 2 == 0 else 'Deu ímpar')
    match imparpar:
        case 'P':
            if total % 2 == 0:
                print ("Você ganhou")
                cont+=1
            else:
                break
        case 'I':
            if total % 2 == 0:
                print ('Você perdeu')
                break
            else:
                print ('Você ganhou')
                cont+=1          
print ('Obrigado por jogar')
if cont == 0:
    print ('Você não ganhou nenhuma vez')
elif cont == 1:
    print (f'Você ganhou {cont} vez') 
    #Só coloquei isso aqui porque tava me irritando ganhou 1 vezes 
else:    
    print(f'Você ganhou {cont} vezes')
