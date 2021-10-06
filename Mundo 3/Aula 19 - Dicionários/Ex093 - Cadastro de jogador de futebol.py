jogador = {'nome': str(input('Nome do jogador: ')).capitalize()}
jogador['partidas'] = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
jogador['gols'] = []
jogador['total de gols'] = 0
for g in range(jogador['partidas']):
    gol = int(input(f'Quantos gols na {g + 1}° partida : '))
    jogador['gols'].append(gol)
    jogador['total de gols'] += gol
print('<>' * 40)
print(jogador)
print('<>' * 40)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('<>' * 40)
print(f'O jogador {jogador["nome"]} jogou {jogador["partidas"]} partidas')
for p, g in enumerate(jogador['gols']):
    print(f'    Na {p+1}° partida, fez {g} gols')
print(f'Totalizando {jogador["total de gols"]} gols')
print('<>' * 40)
print(jogador)