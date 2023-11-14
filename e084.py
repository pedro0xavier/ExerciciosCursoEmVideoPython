''' Faça um programa que leia nome e peso de várias pessoas,                                      guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.B) Uma listagem com as pessoas mais pesadas.C) Uma listagem com as pessoas mais leves.'''
dados = list()
pessoa = list()
while True:
    dados.append(str(input('Nome:' )))
    dados.append(float(input('Peso:' )))
    pessoa.append(dados[:])
    dados.clear()
    resp = str(input('Quer continuar?: [S/N]')).strip().upper()[0]
    if resp in 'N':
        break
print(dados)
maior = max(p[1] for p in pessoa)
menor = min(p[1] for p in pessoa)
nomesmaior = [p[0] for p in pessoa if p[1] == maior]
nomesmenor = [p[0] for p in pessoa if p[1] == menor]
print(f'Foram contabilizadas {len(pessoa)}')
print(f'O maior peso foi {maior} de ',end='')
print(''.join(nomesmaior))
print(f'O maior peso foi {menor} de ',end='')
print(''.join(nomesmenor))


