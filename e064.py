num = 0
contagem = 0 
soma = 0
num = int(input('Digite um número [999] para parar: '))
while num != 999:
    contagem +=1
    soma += num
    num = int(input('Digite um número [999] para parar: '))
print (f'Soma dos números digitados é {soma} e foram digitados {contagem} números')