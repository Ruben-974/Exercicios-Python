novo = ' '
lista = []
while novo not in 'N':
    novo = ' '
    n = int(input('Digite um número: '))
    lista.append(n)
    while novo not in 'NS':
        novo = str(input('Deseja adicionar mais um número? [S/N]: ')).upper().strip()
print('\033[1;34m=-' * 30)
print(f'Foram digitados {len(lista)} números!')
lista.sort(reverse=True)
print(f'A ordem decrescente dos números e {lista}')
if 5 in lista:
    print('O valor 5 se encontra na lista!')
else:
    print('O valor 5 não se encontra na lista!')
print('=-' * 30)