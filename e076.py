items = ('Caderno', 15.56,
         'Lápis', 5,
         'Celular', 1600.90,
         'Monitor', 750.98,
         'Mouse', 200.76,
         'Bola', 23.50
         )
for i in range(0,len(items)):
    if i % 2 == 0:
        print(f'{items[i]:.<30}', end='')
    else:
        print (f'R${items[i]}' )    