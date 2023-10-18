#Programa que leia duas notas e calcule sua média, mostrando uma mensagem no final

n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
soma = n1 + n2
media = soma / 2
print ('Tirando {:.1f} e {:.1f} a média do aluno é de {:.1f}'.format(n1,n2,media))
if media < 5.0:
    print ('Reprovado!!!!')
elif 7> media >= 5.0 :
    print ('Em recuperção!!!!') 
else:
    print ('Aprovado!!!!!!!!!!')    