#Programa que recebe dois valores inteiros e indica se um é maior que o outro ou são iguais

n1 = int(input('Primeiro número: ')) # Primeiro input
n2 = int(input('Segundo número: ')) # Segundo input 

if (n1 > n2): 
    print ('O primeiro número é maior')
elif (n2 > n1):
    print ('O segundo número é maior')
else:
    print ('Os números são iguais')       
