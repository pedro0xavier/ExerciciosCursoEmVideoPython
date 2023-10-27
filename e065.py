cont ='S'
menor = maior = contagem = media = soma = 0
while cont in 'sS':
    num = int(input('Digite um número: '))
    if cont != 'S':
        break
    soma += num
    contagem += 1
    if contagem == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    media = soma / contagem
    cont = str(input('Quer continuar? [S/N]')).upper().strip()[0]
print(f'Você digitou {contagem} números e tem a média de {media}')
print(f'O maior número digitado foi {maior} e o menor número digitado foi {menor}')