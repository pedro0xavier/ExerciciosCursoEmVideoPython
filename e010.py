#Programa que leia quantos reais a pessoa possui na coarteira e converta para outras moedas
real = float(input('Digite quantos reais a carteira possui '))
dolar = real / 5.040
euro = real / 5.324
yen = real / 0.034
print ('Você possiu na sua carteira R${:.2f} que dá {:.3f}$, {:.3f}€ e {:.3f}¥'.format(real,dolar,euro,yen))