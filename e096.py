print ('Controle de terrenos')
print('-=-' * 34)


def area(largura,comprimento):
    area = largura * comprimento
    print (f'A área do terreno {largura}x{comprimento} é de {area:.2f} m²')
l = float(input('Largura: '))
c = float(input('Comprimento: '))
area(l,c)