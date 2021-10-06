n = (int(input('Digite um número: ')), int(input('Digite um número: ')), int(input('Digite um número: ')), int(input('Digite um número: ')))
cont9 = cont3 = 0
print('Você digitou os valores', n)

#for c in n:
#    if c == 9:
#        cont9 += 1
#print(f'O valor 9 apareceu {cont9}x')

print(f'O valor 9 apareceu {n.count(9)}x')

#for c in n:
#    cont3 += 1
#    if c == 3:
#        break
#print(f'O valor 3 apareceu na {cont3}ª posição')

if 3 in n:
    print(f'O valor 3 apareceu na {n.index(3)+1}ª posição')
else:
    print('O valor 3 não apareceu em nenhuma posição')

print('Os valores pares digitados são: ', end='')
for c in n:
    if c % 2 == 0:
        print(c, end=' ')