palavras = 'Pedra','Chao','Campeao','X','Mar','Olhar','Pluma','Turma','Elegante'
vogais = 'a','e','i','o','u'
for p in palavras:
    print (f'A palavra {p}',end='')
    print(' tem as vogais ',end='')
    for v in vogais:
        cont = p.count(v)
        if cont > 0:
            print (v,end='')
    print('\n')        