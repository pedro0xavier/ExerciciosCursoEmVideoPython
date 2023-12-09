def aumentar(preco,taxa,formato = False):
    res = preco + (preco * taxa / 100)
    return res if not formato is False else moeda(res)

def diminuir(preco = 0 ,taxa = 0,formato = False):
    res = preco - (preco * taxa / 100)
    return res if not formato is False else moeda(res)


def dobro(preco = 0,formato = False):
    res = 2 * preco
    return res if not formato is False else moeda(res)


def triplo(preco = 0,formato = False):
    res = 3 * preco
    return res if not formato is False else moeda(res)

def moeda(preco = 0,moeda = 'R$'):
    return f'{moeda}{preco:.2f}'.replace('.',',')