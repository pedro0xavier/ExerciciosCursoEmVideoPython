'''Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.'''
def mensagem (msg):
    tam = len(msg) + 7
    print('-'* tam)
    print(msg)
    print('-'* tam)
mensagem('Pedro')
mensagem('Luca')