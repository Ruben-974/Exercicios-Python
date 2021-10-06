def jogador(nome='- Desconhecido -', gols=0):
    print(f'O jogador {nome} fez {gols} gol(s) no compeonato!')


n = str(input('Nome do jogador: '))
g = str(input('Quantos gols? '))
if g.isnumeric():
    int(g)
else:
    g = 0
if n == '':
    jogador(gols=g)
else:
    jogador(n, g)
