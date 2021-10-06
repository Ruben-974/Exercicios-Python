soma = 0
total = 0
for n in range(1, 501, 2):
    if n % 3 == 0:
        soma += n
        total += 1
print('O total de números é de {}, e a soma deles e de {}'.format(total, soma))
