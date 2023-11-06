numeros = ('Zero','Um','Dois','Três', 'Quatro', 'Cinco','Seis','Sete','Oito','Nove','Dez','Onze','Doze','Treze','Catorze','Quinze','Dezesseis', 'Dezessete', 'Dezoito','Dezenove','Vinte')
while True:
    while True:
        num = int(input('Digite um número de 0 a 20: '))
        if num < 0 or num > 20:
            print ('Número inválido', end=' ')
        else:
            break
    print (f'Digitou o número {numeros[num]}')               
    resp = str(input('Quer continuar?')).strip().upper()[0]
    match resp:
        case 'S':
            num = str(input('Digite o número que quer digitar por extenso: ')).strip().title()
            if num in numeros:
                indexo = numeros.index(num)
                print (f'O número digitado em extenso é {indexo}')
        case 'N':
            break     
