'''Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.'''
lista = []
while True:
    n = int(input('Digite um número: '))
    if n not in lista:
        lista.append(n)
        print ('Número adicionado com sucesso')
    else:
        print ('Número repetido....')
        print ('Número não adicionado')
    resp = str(input('Quer continuar?: ')).strip().upper()[0]            
    if resp in'N':
       break    
print(sorted(lista))