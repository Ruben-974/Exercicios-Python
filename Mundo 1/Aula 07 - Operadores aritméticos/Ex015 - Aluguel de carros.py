dias = int(input('Quantos dias você ficou com o carro? '))
km = float(input('Quantos KM você andou com o carro? '))
pagar = (dias * 60) + (km * 0.15)
print('Você terá que pagar R${} pelo aluguel do carro!'.format(pagar))
