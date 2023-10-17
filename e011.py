# programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária pintá-la
largura = float(input('Largura da parede: '))
altura = float(input('Altura da parede: '))
area = largura * altura
ltinta =  area / 2
print ('Sua parede tem a dimensão de {}x{} e uma área de {:.2f}m²'.format(largura,altura,area))
print ('Para pintar a parede você precisará de {:.2f} litros de tinta'.format(ltinta))