n1 = int(input('Digite um valor: '))
n2 = int(input('Digite um valor: '))
p = 0
while p != 5:
    print('''
[ 1 ] Somar
[ 2 ] Multiplicar
[ 3 ] Maior
[ 4 ] Digitar novos números
[ 5 ] Sair do programa
''')
    p = int(input('Digite a sua opção: '))
    print('')
    if p == 1:
        n3 = n1 + n2
        print('O resultado {} + {} = {}'.format(n1, n2, n3))
    elif p == 2:
        n3 = n1 * n2
        print('O resultado de {} x {} = {}'.format(n1, n2, n3))
    elif p == 3:
        if n1 > n2:
            print('O número {} e maior que {}'.format(n1, n2))
        elif n2 > n1:
            print('O número {} e maior que {}'.format(n2, n1))
        elif n1 == n2:
            print('O número {} e igual {}, portando não ha número maior'.format(n1, n2))
    elif p == 4:
        print('Informe os números novamente!')
        print('')
        n1 = int(input('Valor do primeiro número: '))
        n2 = int(input('Valor do segundo número: '))
    elif p == 5:
        print('PROGRAMA FINALIZADO!')
    else:
        print('Opção invalida! Tente novamente.')
