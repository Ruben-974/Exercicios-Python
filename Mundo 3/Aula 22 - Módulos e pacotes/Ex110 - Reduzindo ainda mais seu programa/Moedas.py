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


def resumo(n=0, a=10, d=5):
    print('-' * 30)
    print(f'{"Resumo Do Preço":^30}')
    print('-' * 30)
    print(f'{" Preço analisado:":<20}{moeda(n)}')
    print(f'{" Dobro do Preço:":<20}{dobro(n, True)}')
    print(f'{" Metade do Preço:":<20}{metade(n, True)}')
    print(f'{f" {a}% de aumento:":<20}{aumentar(n, a, True)}')
    print(f'{f" {d}% de redução:":<20}{diminuir(n, d, True)}')
    print('-' * 30)
