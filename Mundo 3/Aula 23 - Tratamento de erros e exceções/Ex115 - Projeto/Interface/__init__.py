def linha(quant=50, caracter='-'):
    print(caracter * quant)


def titulo(txt, centralizar=50, cor=0, formato=0):
    linha()
    print(f'\033[{formato};{cor}m{txt:^{centralizar}}\033[m')
    linha()


def opções(lista):
    titulo(txt='~-~ MENU PRINCIPAL ~-~', cor=33, formato=1)
    pos = 0
    quantop = []
    for item in lista:
        pos += 1
        quantop.append(str(pos))
        print(f'\033[1;37m{pos}\033[m - \033[1;37m{item}\033[m')
    linha()
    while True:
        res = str(input('Qual e a sua escolha? '))
        if res not in quantop:
            print('\033[31;1mERRO: Você escolheu um opção invalida!\033[m')
        else:
            return res

