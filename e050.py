soma = 0
contagem = 0
for i in range (0,6):
    num  = int(input('Digite um número: '))
    if num % 2 == 0:
        contagem+=1
        soma+=num
print ('Foram informados {} números pares e a soma de todos eles é {}'.format(contagem,soma))          
