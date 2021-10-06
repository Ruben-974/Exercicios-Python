def fatorial(num=0, show=False):
    """
    -> Calcular Fatorial
    :param num: Valor do Fatorial
    :param show: Mostrar processo da expressão (Opcional)
    :return: Retorna o valor do fatorial de "num"
    """
    fac = 1
    for n in range(0, num):
        if show:
            print(num, end=' ')
            if num != 1:
                print('x', end=' ')
            else:
                print('=', end=' ')
        fac *= num
        num -= 1
    print(fac)


fatorial(6, show=True)
help(fatorial)
