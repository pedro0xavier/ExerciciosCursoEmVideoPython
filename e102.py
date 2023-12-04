def fatorial(num,show):
    fact = 1
    c = 0
    for c in range(num , 0,-1):
        if show:
            if c >= 1:
                print(f'{c} ',end='')
            if c > 1:
                print('X',end=' ')
            fact*=c
            if c == 1:
                print(f' =  {fact}')
    return fact
print(fatorial(5,show = True))