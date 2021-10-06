from random import randint
from time import sleep
print('<>' * 25)
print(f'{"JOGA NA MEGA SENA":^50}')
print('<>' * 25)
quantidade = int(input('Quantos jogos você quer que eu sorteie? '))
sorteados = []
n = 0
for q in range(0, quantidade):
    while len(sorteados) != 6:
        n = randint(1, 60)
        if n not in sorteados:
            sorteados.append(n)
    sorteados.sort()
    print(f'Jogo {q + 1}: {sorteados}')
    sleep(1)
    sorteados.clear()
print('<>' * 25)
print(f'{"BOA SORTE!":^50}')
print('<>' * 25)
