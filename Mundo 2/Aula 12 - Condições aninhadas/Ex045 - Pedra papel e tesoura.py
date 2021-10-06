from random import randint
from time import sleep
print('''JOGO PEDRA, PAPEL, TESOURA
ESCOLHA UMA OPÇÂO:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
jogador = int(input('Qual vai ser a sua jogada? '))
print('JO.')
sleep(1)
print('KEN..')
sleep(1)
print('PÔ...')
sleep(1)
print('-*' * 15)
print('O computador escolheu {}'.format(itens[computador]))
print('O jogador escolheu {}'.format(itens[jogador]))
print('-*' * 15)
if computador == 0:
    if jogador == 0:
        print('\033[1;33mEMPATE\033[0m')
    elif jogador == 1:
        print('\033[1;32mJOGADOR VENCE\033[0m')
    elif jogador == 2:
        print('\033[1;31mCOMPUTADOR VENCE\033[0m')
if computador == 1:
    if jogador == 1:
        print('\033[1;33mEMPATE\033[0m')
    elif jogador == 2:
        print('\033[1;32mJOGADOR VENCE\033[0m')
    elif jogador == 0:
        print('\033[1;31mCOMPUTADOR VENCE\033[0m')
if computador == 2:
    if jogador == 2:
        print('\033[1;33mEMPATE\033[0m')
    elif jogador == 0:
        print('\033[1;32mJOGADOR VENCE\033[0m')
    elif jogador == 1:
        print('\033[1;31mCOMPUTADOR VENCE\033[0m')
