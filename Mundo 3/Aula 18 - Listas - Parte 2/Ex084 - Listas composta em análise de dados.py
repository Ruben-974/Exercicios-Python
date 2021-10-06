dados = []
pessoa = []
continuar = ' '
pessoap = []
pessoal = []
while continuar != 'N':
    continuar = ' '
    pessoa.append(str(input('Nome: ')).capitalize())
    pessoa.append(float(input('Peso: ')))
    dados.append(pessoa[:])
    leve = pesado = dados[0][1]
    pessoa.clear()
    while continuar not in 'SN':
        continuar = str(input('Cadastrar nova pessoa? [S/N]: ')).upper().strip()
for c in dados:
    if c[1] > pesado:
        pesado = c[1]
    if c[1] < leve:
        leve = c[1]
for c in dados:
    if c[1] == pesado:
        pessoap.append(c[0])
    if c[1] == leve:
        pessoal.append(c[0])
print(f'Você cadastrou {len(dados)} pessoas'
      f'\nO peso mais pesado foi {pesado}Kg, pessoas com esse peso são {pessoap}'
      f'\nO peso mais leve foi {leve}Kg, pessoas com essa peso são {pessoal}')
