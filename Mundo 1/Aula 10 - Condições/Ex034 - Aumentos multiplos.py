s = float(input('Qual e o seu salario: R$'))
if s >= 1250:
    print('Você receberá 10% de aumento, totalizando: R${:.2f}'.format((s * 10 / 100)+s))
else:
    print('Você receberá 15% de aumento, totalizando: R${:.2f}'.format((s * 15 / 100)+s))
