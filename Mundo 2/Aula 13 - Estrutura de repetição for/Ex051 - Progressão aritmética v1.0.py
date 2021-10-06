print('10 primeiros termos')
n1 = int(input('Primeiro termo: '))
n2 = int(input('Razâo: '))
n3 = n1 + (10-1) * n2
for c in range(n1, n3, n2):
    print(c, end=' - ')
print('FIM')
