contagem = soma = n = 0
while True:
    n = int(input('Digite um número 999 para parar '))
    if n == 999:
        break
    soma+=n
    contagem+=1
print (f'Você digitou {contagem} números que deram uma soma de {soma}')    
