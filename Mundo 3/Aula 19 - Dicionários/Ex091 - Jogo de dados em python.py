from random import randint
from time import sleep
from operator import itemgetter
print('Valores sorteados:')
jogadas = {}
organizado = {}
for s in range(0, 4):
    jogadas[f'jogador{s + 1}'] = randint(1, 6)
for k, v in jogadas.items():
    sleep(1)
    print(f'{k} tirou {v} no dado')
print('<>' * 19)
print('     == RANKING DOS JOGADORES ==')
organizado = sorted(jogadas.items(), key=itemgetter(1), reverse=True)
for k, v in enumerate(organizado):
    sleep(1)
    print(f'Em {k + 1}° lugar foi {organizado[k][0]} com o valor {organizado[k][1]}')
