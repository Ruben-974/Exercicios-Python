numeros = []
for c in range(0, 5):
    maior = menor = c
    n = int(input(f'Digite um valor para a posição {c}: '))
    numeros.append(n)
    for v in numeros:
        if v > maior:
            maior = v
        if v < menor:
            menor = v
print('-=' * 30,
      f'\nVocê digitou os valores {numeros}')
print('-=' * 30,
      f'\nO maior número foi {maior}, nas posições ', end='')
for pos, num in enumerate(numeros):
    if num == maior:
        print(pos, end='...')
print(f'\nO menor número foi {menor}, nas posições ', end='')
for pos2, num2 in enumerate(numeros):
    if num2 == menor:
        print(pos2, end='...')
print('\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')