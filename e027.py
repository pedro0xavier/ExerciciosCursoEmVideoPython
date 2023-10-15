nome = str(input('Digite seu nome completo ')).strip()
nsplit = nome.split()
print('Seu primeiro nome é {}'.format(nsplit[0]))
print('Seu último nome é {}'.format(nsplit[-1]))
