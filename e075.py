nums = ['','','','']
contpares = cont9 = 0
pares = []
for i in range (0,4):
    n = int(input('Digite um número: '))
    nums[i] = n
    if n % 2 == 0:
        pares.insert(i,n)
        contpares+=1     
print (f'Os números digitados foram {tuple(nums)}')
if 9 in nums:
    print (f'O valor 9 apareceu {nums.count(9)} vez')
else:
    print (f'O número 9 foi digitado nenhuma vez')
if 3 in nums:
    print (f'O número 3 foi digitado pela primeira vez na posição {nums.index(3)+1}')    
else:
    print (f'O número 3 não foi digitado nenhuma vez')    
if contpares == 0:
    print ('Não foram diigtados nenhum número par')        
else:
    if contpares == 1:
        print ('Só foi digitado somente o número par ', end='')        
    if contpares > 1:
        print ('Foram digitados os números ', end='')    
    for x in pares:
        print(f'{x} ',end='')