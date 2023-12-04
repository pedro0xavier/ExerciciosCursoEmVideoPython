def fatorial(num,show):
    fact = 1
    c = 0
    for i in range(num,0,-1):
        fact *= i
    if show:
        print(f'{num}',end='')
        for c in range(num - 1, 0,-1):
            print(f' X {c}',end='')
            if c == 1:
                print(f' =  {fact}')
    return fact
print(fatorial(9,show = True))