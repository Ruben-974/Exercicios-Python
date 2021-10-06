def dobro(n, form=False):
    d = n * 2
    return d if form is False else moeda(d)

def metade(n, form=False):
    m = n / 2
    return m if form is False else moeda(m)


def aumentar(n, p, form=False):
    a = n + (n * (p / 100))
    return a if form is False else moeda(a)


def diminuir(n, p, form=False):
    d = n - (n * (p / 100))
    return d if form is False else moeda(d)


def moeda(n):
    moe = f'{n:.2f}'
    moe = str(f'R${moe.replace(".", ",")}')
    return moe
