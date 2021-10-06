preço = mais1000 = total = barato = cont =0
print('LOJA DO PERIGO')
nb = ''
while True:
    continuar = ' '
    produto = str(input('Nome do Produto: '))
    preço = float(input('Preço: R$ '))
    cont += 1
    while continuar not in 'NS':
        continuar = str(input('Deseja continuar? [N/S]: ')).strip().upper()[0]
    total += preço
    if preço > 1000:
        mais1000 += 1
    if cont == 1 or preço < barato:
        barato = preço
        nb = produto
    if continuar in 'N':
        print('FIM DA COMPRA!')
        break
print(f'O total da compra foi de R${total}')
print(f'Temos {mais1000} produto custando mais de R$1000.00')
print(f'O produto mais barato foi {nb} que custa {barato}')