time = []
gols = []
cod = tentativa = 0
jogador = {'codigo': 0, 'nome': str, 'partidas': int, 'gols': 0, 'totgols': 0}
while True:
    jogador['nome'] = str(input('Nome do jogador: ')).capitalize()
    jogador['partidas'] = int(input(f'{jogador["nome"]} jogou quantas partidas? '))
    for g in range(jogador['partidas']):
        gol = int(input(f'Quantos gols na partida {g + 1}: '))
        jogador['totgols'] += gol
        gols.append(gol)
    jogador['gols'] = gols.copy()
    time.append(jogador.copy())
    gols.clear()
    while True:
        res = str(input('Cadastrar novo jogador? [S/N]: ')).upper()[0]
        if res in 'NS':
            break
        print('ERRO! Valor invalido! Tente novamente!')
    jogador['totgols'] = 0
    if res == 'N':
        break
for c in range(len(time)):
    time[c]['codigo'] = c
print('<>' * 20)
print('Cod   Nome        gols             Total')
print('--' * 20)
for j in time:
    print(f'{j["codigo"]:>3}   {j["nome"]:<10}  {str(j["gols"]):<15}  {j["totgols"]:}')
print('--' * 20)
while cod != 999:
    cod = int(input('Mostrar dados de qual jogador? (999 para parar): '))
    for j in time:
        if j['codigo'] == cod:
            tentativa += 1
            print(f'- LEVANTAMENTO DO JOGADOR > {j["nome"]} <')
            for p, g in enumerate(j['gols']):
                print(f'No {p + 1}° jogo fez {g} gols')
                tentativa = 0
        if tentativa == len(time):
            tentativa = 0
            print('Codigo invalido! Tente novamente!')
print('<<< FINALIZADO >>>')
