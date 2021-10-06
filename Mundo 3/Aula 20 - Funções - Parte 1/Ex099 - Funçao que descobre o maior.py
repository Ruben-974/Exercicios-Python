from time import sleep


def maior(*num):
    maior = 0
    print('--' * 30)
    print('Analizando valores...')
    if len(num) > 0:
        maior = num[0]
    for n in num:
        print(n, end=' ')
        sleep(0.5)
        if n > maior:
            maior = n
    print(f'Foram informados, tendo um total de {len(num)} valores ')
    print(f'E o maior valor foi {maior}')


maior(5, 3, 7, 9, 1, 1)
maior(5, 1, 3)
maior(7, 9)
maior(2)
maior()
