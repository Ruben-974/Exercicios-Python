print('OS 10 PRIMEIROS TERMOS DE UMA PA')
n1 = int(input('Primeiro termo: '))
n2 = int(input('Razão da PA: '))
n3 = n1 + (10 - 1) * n2
while n1 < n3:
    n1 += n2
    print(n1 - n2, end=' - ')
print('FIM')