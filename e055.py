maior = 0
menor = 0
for i in range (0,5):
    peso = float(input('Digite o seu peso: '))
    if i == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso <  menor:
            menor = peso
print ('O menor peso apresentado foi {} e o maior peso apresentado foi {}'.format(menor,maior))    
