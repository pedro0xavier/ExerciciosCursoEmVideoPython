first = (int(input('Primeiro termo: ')))
razao = int (input('Razão: '))
decimo = first + (10 - 1) * razao
for c in range (first,decimo + razao,razao):
    print ('{}'.format(c), end = ' ')
