'''Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular e outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.'''
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