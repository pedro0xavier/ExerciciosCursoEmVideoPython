# Programa que leia um número inteiro qualquer e peça para o usuário escolher a base de conversão entre binário,octal e hexadecimal

n = int(input('Digite um número inteiro: '))
print ('Escolha uma das opções de bases para conversão:  ')
print ('[1] converter para hexadecimal ')
print ('[2] converter para octal')
print ('[3] converter para binário')
opcao = int(input('Sua opção: '))
match opcao: #Match case ao invés de if elif 
    case 1:
        print ('{} convertido para hexadecimal é {}'.format(n,hex(n)[2:]))
    case 2:
        print ('{} convertida para octal é {}'.format(n,oct(n)[2:]))
    case 3:
        print ('{} convertida para binário é {}'.format(n,bin(n)[2:]))
    case other:
        print ('O número inserido não é válido')