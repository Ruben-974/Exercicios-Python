produtos = ('Caderno', 5.99, 'Lapis', 1.50, 'Mochila', 90.50)
print('-' * 50)
print(f'{"Tabela de Preços":^50}')
print('-' * 50)
for c in range(0, len(produtos)):
    if c % 2 == 0:
        print(f'{produtos[c]:.<41}', end='R$ ')
    if c % 2 != 0:
        print(f'{produtos[c]:>5.2f}')
print('-' * 50)
