def leiafloat(txt):
    while True:
        try:
            n = float(input(txt))
        except ValueError:
            print(f'\033[1;31mERRO: Você digitou um valor invalido!\033[m')
        else:
            return n


def leiaint(txt):
    while True:
        try:
            n = int(input(txt))
        except ValueError:
            print(f'\033[1;31mERRO: Você digitou um valor invalido!\033[m')
        else:
            return n


#res = leiaint('Digite um número inteiro: ')
#print(res)
#res = leiafloat('Digite um número real: ')
#print(res)