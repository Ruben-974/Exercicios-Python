km = float(input('Quantos KM, você está agora? '))
m = km - 80
m1 = m * 7
if km <= 80:
    print('Tudo ok, você esta dentro do permitido!')

else:
    print('Você esta fora do limite, você irá pagar uma multa de R$7 por cada KM ultrapassado!')
    print('A multa será de {:.2f}, por ter passado {:.2f}KM do permitido.'.format(m1, m))