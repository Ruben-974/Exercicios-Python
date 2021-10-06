res = ''
dados = {}
cadastrados = []
media = 0
while res in 'S':
    res = ''
    dados.clear()
    dados['nome'] = str(input('Nome: ').capitalize())
    while True:
        dados['sexo'] = str(input('Sexo [M/F]: ')).upper().strip()
        if dados['sexo'] in 'MF':
            break
        else:
            print('ERRO! Digite um valor valido!')
    dados['idade'] = int(input('Idade: '))
    while True:
        res = str(input('Cadastrar nova pessoa? [S/N]: ')).upper().strip()
        if res in 'NS':
            break
        else:
            print('ERRO! Digite um valor valido!')
    cadastrados.append(dados.copy())
for c in cadastrados:
    media += c['idade']
media = media / len(cadastrados)
print('<>' * 20)
print(f'A) Ao todo temos {len(cadastrados)} pessoas cadastradas!')
print(f'B) A media de idade e de {media:.2f} anos')
print(f'C) As mulheres cadastradas foram ', end='')
for c in cadastrados:
    if c['sexo'] == 'F':
        print(f'{c["nome"]}', end=' ')
print()
print('D) Pessoas acima da media:', end='')
for c in cadastrados:
    if c['idade'] > media:
        print()
        for k, v in c.items():
            print(f'{k} = {v};', end=' ')
print()
print('<>' * 20)
