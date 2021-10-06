def analisedinheiro(txt):
    while True:
        v = input(txt).strip()
        original = v
        v = v.replace(',', '.')
        if v.replace('.', '').isnumeric():
            v = float(v)
            return v
        else:
            print(f'\033[1;31mERRO: O valor "{original}" é invalido!\033[m')


#dinheiro = analisedinheiro('Digite o preço: ')
#print(dinheiro)