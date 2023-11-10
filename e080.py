'''Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.'''
listanum = list()
for i in range(0,5):
    n = int(input('Digite um número: '))
    if i == 0:
        listanum.append(n)
    else:
        if n > listanum[-1] or n > listanum[-1]:
            listanum.append(n)
        else:    
            for pos, x in enumerate(listanum):
                if n <= x:
                    listanum.insert(pos, n)
                    break
print(listanum)