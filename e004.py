#Faça um programa que leia algo digitado pelo teclado e mostre na tela o tipo primitivo e todas as informações sobre ela
n = input("Digite algo ")

print('O tipo primitivo desse valor é {}'.format(type(n)))

print('Tem espaços?', n.isspace())
print("É um número?", n.isnumeric())
print("Tem letras maiúsculas?", n.isupper())
print("Tem letras minúsculas?", n.islower())
print("É capitalizada?", n.istitle())
#se tu escrever uma palavra tipo Python ele reconhece como capitalizada
print("É uma palavra?", n.isalpha())
# a variável n é um objeto que tem características e realiza funcionalidades,(atributos e métodos(is alpha é um método por exemplo))
print("É alfanumérico?", n.isalnum())
print("É um número decimal?", n.isdecimal())
print("É ASCII?", n.isascii())
 