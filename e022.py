'''Um programa que leia o nome completo de uma pessoa e mostre o nome com todas as letras maiúsculas e minúsculas,quantas letras ao todo e quantas letras tem o primeiro nome.'''
nome = str(input('Digite seu nome completo ')).strip()
print('Analisando seu nome.....')

print('Seu nome em maiúsculas é {}'.format(nome.upper()))
print('Seu nome em minúsuclas é {}'.format(nome.lower()))
print('Seu nome ao todo tem {} letras '.format(len(nome)-nome.count(' ')))
x = nome.split()
print('Seu primeiro nome é {} e tem {} letras'.format((x[0]),len(x[0])))
