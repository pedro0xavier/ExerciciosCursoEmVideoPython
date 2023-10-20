num = int(input('Digite um número: '))
if num <= 1:
    print ('Não é um número primo')
else:
    for c in range(1,num):
        if (num % c == 0):
            print ('{} não é um número primo'.format(num))
            break
        else:
            print ('{} é um número primo'.format(num))
            break