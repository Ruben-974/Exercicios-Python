soma = 0
n = int(input('Digite um número: '))
for c in range(1, n+1):
    if n % c == 0:
        soma += 1
print('O número {} e divisivel por outros {} números'.format(n, soma))
if soma == 2:
    print('O NÚMERO E PRIMO')
else:
    print('O NÚMERO NÃO E PRIMO')
