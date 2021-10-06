from random import randint
n = (randint(1, 9), randint(1, 9), randint(1, 9), randint(1, 9), randint(1, 9))
print('Os números sorteados foram: ', end='')
for c in n:
    print(c, end=' ')
print(f'\nO maior valor sorteado foi: {max(n)}')
print(f'O menor valor sorteado foi: {min(n)}')
