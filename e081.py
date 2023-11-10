''' Crie um programa que vai ler vários números e colocar em uma lista.Depois disso, mostre:A) Quantos números foram digitados.B) A lista de valores, ordenada de forma decrescente.C) Se o valor 5 foi digitado e está ou não na lista.
'''
lista = []
while True:
    lista.append(int(input('Digite um número: ')))
    resposta = str(input('Quer continuar?: ')).strip().upper()[0]
    if resposta in 'nN':
        break
lista.sort(reverse=True)
print(f'Você digitou {len(lista)} elementos')
print('O número 5 faz parte da lista' if 5 in lista else 'O número 5 não faz parte da lista')
print (lista)