matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somapar = somacoluna = maiorlinha = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para a posição ({l}, {c}): '))
        maiorlinha = matriz[l][c]
print('><' * 25)
for l in range(0, 3):
    print()
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            somapar += matriz[l][c]
        if c == 2:
            somacoluna += matriz[l][c]
        if l == 1:
            if matriz[1][c] > maiorlinha:
                maiorlinha = matriz[1][c]
print('\n')
print('><' * 25)
print(f'\nA soma dos valores pares são: {somapar}'
      f'\nA soma dos valores da coluna 3 e: {somacoluna}'
      f'\nO maior valor da linha 2 e: {maiorlinha}')
print()
print('><' * 25)
