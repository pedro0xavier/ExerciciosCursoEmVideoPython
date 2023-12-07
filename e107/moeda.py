def aumentar(preco,taxa):
    res = preco + (preco * taxa / 100)
    return res


def diminuir(preco,taxa):
    res = preco - (preco * taxa / 100)
    return res


def dobro(preco):
    res = 2 * preco
    return res


def triplo(preco):
    res = 3 * preco
    return res