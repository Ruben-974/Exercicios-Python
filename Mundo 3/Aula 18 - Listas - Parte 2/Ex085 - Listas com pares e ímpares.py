numeros = [[], []]
for c in range(0, 7):
    n = int(input(f'Digite o {c + 1}° número: '))
    if n % 2 == 0:
        numeros[0].append(n)
    if n % 2 != 0:
        numeros[1].append(n)
numeros[0].sort()
numeros[1].sort()
print(f'Os valores pares digitados foram: {numeros[0]}'
      f'\nOs valores ímpares foram: {numeros[1]}')