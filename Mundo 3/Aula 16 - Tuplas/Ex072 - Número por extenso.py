p = ('Zero', 'Um', 'Dois', 'Três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'cartoze', 'quinze', 'dezeseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')
novo = ' '
while novo not in 'N':
    novo = ' '
    n = int(input('Digite um número de 0 a 20: '))
    if n < 0 or n > 20:
        print('Tente novamente!', end=' ')
    if 0 <= n <= 20:
        print(f'O número digitado foi {p[n]}')
        while novo not in 'SN':
            novo = str(input('Deseja digitar um novo número? [S/N]: ')).upper().strip()
            if novo == 'N':
                break

