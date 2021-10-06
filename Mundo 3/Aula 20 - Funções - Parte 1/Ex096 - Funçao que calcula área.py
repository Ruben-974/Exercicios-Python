def area():
    print('-------- Calcular área --------')
    l = float(input('Qual a lagura? (M): '))
    c = float(input('Qual o comprimento? (M): '))
    a = l * c
    print(f'A área {l}x{c} e igual á: {a:.2f}')
    print('-' * 31)


while True:
    area()
    while True:
        res = str(input('Calcular área novamente? [N/S]: ')).upper().strip()[0]
        if res in 'SN':
            break
        print('Valor invalido! Tente novamente!')
    if res == 'N':
        break
print('--------- FINALIZADO ---------')