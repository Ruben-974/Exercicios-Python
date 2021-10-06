n1 = int(input('\033[4;35mPrimeiro número:\033[0m '))
n2 = int(input('\033[4;35mSegundo número:\033[0m '))
s1 = int(n1 + n2)
print('A soma de {} com {} e igual a {}{}{}!'.format(n1, n2, '\033[33m', s1, '\033[0m'))
