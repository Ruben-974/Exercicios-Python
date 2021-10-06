from random import randint
from time import sleep
sorteados = []


def sortear():
    print('-' * 55)
    print(' Sorteando 5 valores para a lista: ', end='')
    for s in range(0, 5):
        sorteados.append(randint(0, 9))
        sleep(0.5)
        print(sorteados[s], end=' ')


def somapar():
    soma = 0
    for n in sorteados:
        if n % 2 == 0:
            soma += n
    print(f'\n Somando os valores pares de {sorteados}, temos {soma}')
    print('-' * 55)


sortear()
somapar()
