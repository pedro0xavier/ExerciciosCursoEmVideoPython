frase = str(input('Digite qualquer frase')).strip().upper()     
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]

if inverso == junto:
    print('É um palindromo')
else:
    print ('Não é um palindromo ')    