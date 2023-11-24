from random import randint
from time import sleep
from operator import itemgetter 
numeros = {"jogador1": randint(1,6),
           "jogador2": randint(1,6),
           "jogador3": randint(1,6),
           "jogador4": randint(1,6)}
for ke,it in numeros.items():
    print(f"{ke} tirou {it}")
    sleep(1)
res = dict(sorted(numeros.items(), key=itemgetter(1), reverse=True))
print('-=-'*30)
print('RANKING DE JOGADOR')
i = 1
for ranking,numero in res.items():
    print(f" {i}° lugar {ranking} que tirou o número {numero}")
    sleep(1)
    i+=1