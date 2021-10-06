from math import hypot
n1 = float(input('Qual o valor do cateto oposto? '))
n2 = float(input('Qual o valor do cateto adjacente? '))
n3 = hypot(n1, n2)
print('O resultado da hipotenusa e: {:.2f}'.format(n3))
