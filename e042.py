'''Programa para checar os segmentos de um triângulo edeterminar qual tipo de triângulo pode ser formado e se um triângulo pode ser formado'''

l1 = float(input('Primeiro segmento: '))
l2 = float(input('Segundo segmento: '))
l3 = float (input('Terceiro segmento: '))

if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print ('0s segmentos acima PODEM formar um triângulo')
    if l1 == l2 == l3 == l1:
        print ('O triângulo formado é do tipo equilátero')
    elif l1 != l2 != l3 != l1:
        print ('O triângulo é do tipo isósceles')
    else:
        print ('O triângulo é do tipo escaleno')   
else:
    print ('Os segmentos não podem formar um triângulo')    
