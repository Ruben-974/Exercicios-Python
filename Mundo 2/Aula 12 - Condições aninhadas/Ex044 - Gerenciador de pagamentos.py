print('+_+_+_+_+ LOGINHA DO PERIGO +_+_+_+_+')
valor = float(input('Qual foi o valor das compras? '))
print('''Como você deseja fazer o pagamento?
 [ 1 ] Á vista Dinheiro/Cheque ( 10% de desconto ): 
 [ 2 ] Á vista no cartão ( 5% de desconto ): 
 [ 3 ] Em até 2x no cartão ( Valor normal ): 
 [ 4 ] 3x ou mais no cartão: ( 20% de juros ):''')
pagamento = int(input('Qual vai ser a sua forma de pagamento? '))
if pagamento == 1:
    print('Sua compra de {}, vai ter um desconto de 10%, ficando no valor de R${}'.format(valor, valor - (valor * 10 / 100)))
elif pagamento == 2:
    print('Sua compra de {}, vai ter um desconto de 5%, ficando no valor de R${}'.format(valor, valor - (valor * 5 / 100)))
elif pagamento == 3:
    print('Sua compra de {}, vai ser dividida até 2x sem juros, porém também ficará sem desconto!'.format(valor))
    v1 = int(input('Você pode parcelar em 1x ou 2x, qual vc deseja? '))
    if v1 == 1:
        print('OK, o valor de {}, será parcelado de 1x sem juros!'.format(valor))
    elif v1 == 2:
        print('OK, o valor será parcelado de 2x sem juros, totalizando {} por mês.'.format(valor / 2))
    else:
        print('CALOTEIRO!!! ta achando que e o capitão de ferro, achando q vai dividir mais de 2x sem juros??? :(')
elif pagamento == 4:
    x = int(input('Em quantas x você deseja parcelar? '))
    total = valor + (valor * 20 / 100)
    print('Você ira parcelar o valor de {} com juros de 20% ( R${} ), parcelado em {}x totalizando R${} mensais'.format(valor, total, x, total / x))
else:
    print('Você digitou um valor INVALIDO, tente novamente!')
