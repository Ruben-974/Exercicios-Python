numeros = []
continuar = ' '
while continuar != 'N':
    continuar = ' '
    n = int(input('Digite um número: '))
    if n not in numeros:
        numeros.append(n)
        print('Número adicionado com sucesso!')
    else:
        print('Número repitido! Não irei adicona-lo!')
    while continuar not in 'NS':
        continuar = str(input('Deseja continuar? [S/N]: ')).upper().strip()
numeros.sort()
print(f'Os números foram {numeros}')
