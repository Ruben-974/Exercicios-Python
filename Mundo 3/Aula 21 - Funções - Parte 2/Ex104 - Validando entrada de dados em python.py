def leiaint(msg):
    while True:
        n = input(msg)
        if n.isnumeric():
            return n
        else:
            print('\033[1;31mValor invalido! Tente novamente!\033[0m')


n = leiaint('Digite um número: ')
print(f'Você digitou o número {n}')
