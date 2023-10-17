#Programa que converta uma temperatura digitada em graus celcius e a converta para fahrenheit
celsius = float(input('Digite a temperatura em celcius para ser convertida para fahrenheit '))
fh = (celsius * 1.8) + 32

print ('A temepratura em celcius é {} e após ser convertida para fahrenheit ficou {:.2f}'.format(celsius,fh))