import Moedas
v = float(input('Digite o preço: R$'))
print(f'A metade de {Moedas.moeda(v)} é {Moedas.metade(v, True)}')
print(f'A dobro de {Moedas.moeda(v)} é {Moedas.dobro(v, True)}')
print(f'Aumentando {Moedas.moeda(v)} em 10%, temos no total {Moedas.aumentar(v, 10, True)}')
print(f'Diminuir {Moedas.moeda(v)} em 15%, temos no total {Moedas.diminuir(v, 15, True)}')
