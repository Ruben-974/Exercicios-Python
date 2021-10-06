novo = ' '
lista = []
pares = []
impares = []
while novo not in 'N':
    novo = ' '
    n = int(input('Digite um número: '))
    lista.append(n)
    while novo not in 'NS':
        novo = str(input('Digitar novos valores? [S/N]: ')).upper().strip()
for c in lista:
    if c % 2 == 1:
        impares.append(c)
    if c % 2 == 0:
        pares.append(c)
print('+-' * 30)
print(f'Os valores digitados foram {lista}')
print(f'Os valores pares digitados foram {pares}')
print(f'Os valores impares digitados foram {impares}')
print('+-' * 30)