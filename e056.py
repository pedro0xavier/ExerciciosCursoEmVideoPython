somaidade = 0
nomemaisvelho = 'Pedro'
maioridade = 0
contador = 0
for i in range (1,5):
    print ('{}ª Pessoa'.format(i))
    nome = str(input('Nome da primeira pessoa:')).strip().upper()
    idade = int (input('Idade:'))
    sexo = str(input('Sexo (M/F):')).strip().upper()
    if i == 1:
        nomemaisvelho = ''
        maioridade = 0
    if idade > maioridade:
        nomemaisvelho = nome
        maioridade = idade
    if  sexo == 'M' and idade < 20:
        contador+=1      
    somaidade = somaidade + idade
media = somaidade / 4

print ('A média de idade do grupo é {} anos '.format(media))
print ('O homem mais velho do grupo se chama {} e tem {} anos '.format(nomemaisvelho,maioridade))
print ('Ao todo são {} mulheres abaixo de 20 anos '.format(contador))