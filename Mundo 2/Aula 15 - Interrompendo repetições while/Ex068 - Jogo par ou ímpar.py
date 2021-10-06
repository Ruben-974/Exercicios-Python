from random import randint
vitorias = 0
print('-' * 25)
print('VAMOS JOGAR PAR OU ÍMPAR!')
print('-' * 25)
while True:
    com = randint(0, 10)
    jogador = int(input('Diga um valor: '))
    soma = jogador + com
    pi = ' '
    while pi not in 'P I':
        pi = str(input('Par ou Ìmpar? [P/I]: ')).strip().upper()[0]
        print('-' * 55)
        print(f'Você jogou {jogador} e o computador {com}. Totalizando {soma} ', end='')
        print('DEU PAR' if soma % 2 == 0 else 'DEU ÌMPAR')
        print('-' * 55)
    if soma % 2 == 0 and pi in 'P' or soma % 2 != 0 and pi in 'IÌ':
        vitorias += 1
        print('VOCÊ VENCEU!')
    else:
        print('*-' * 15)
        print('VOCÊ PERDEU!')
        print(f'VOCÊ ME VENCEU {vitorias} VEZES')
        print('*-' * 15)
        break
