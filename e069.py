'''Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:A) quantas pessoas tem mais de 18 anos.B) quantos homens foram cadastrados.C) quantas mulheres tem menos de 20 anos.'''
contadormenos20 = contadormulher= mais18contador = contadorhomem = 0
while True:
    print ('==='*32)
    print ('CADASTRE UMA PESSOA')
    print ('==='*32)
    idade = int(input('Idade: '))
    sexo = ' '
    while not sexo in 'mfMF':
        sexo =  str(input('Sexo: [M/F]')).upper().strip()[0]
        if sexo not in 'MF':
            print ('Opção inválida digite M ou F')
    if idade >= 18:
        mais18contador+=1
    match sexo:
        case 'M':
            contadorhomem+=1
        case 'F':
            contadormulher+=1 # No desafio é junto com a idade mas botei separado
            if idade < 20: 
                contadormenos20+=1         
    continuar = ' '
    while continuar not in 'SsnN':
        continuar =  str(input('Quer continuar?: [S/N]')).upper().strip()[0]    
        if continuar not in 'SN':
            print ('Opção inválida digite S OU N ')
    if continuar in'N':
        break
print (f'Total de pessoas com mais de 18 anos: {mais18contador}')
print (f'Total de homens cadastrados {contadorhomem}')
print (f'Total de mulheres cadastradas {contadormulher}')
print (f'Total de mulheres registradas com menos de 20 anos: {contadormenos20}')