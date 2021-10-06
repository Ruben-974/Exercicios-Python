import Moedas
v = float(input('Digite o preço: R$'))
print(f'A metade de {Moedas.moeda(v)} é {Moedas.moeda(Moedas.metade(v))}')
print(f'A dobro de {Moedas.moeda(v)} é {Moedas.moeda(Moedas.dobro(v))}')
print(f'Aumentando {Moedas.moeda(v)} em 10%, temos no total {Moedas.moeda(Moedas.aumentar(v))}')
print(f'Diminuir {Moedas.moeda(v)} em 10%, temos no total {Moedas.moeda(Moedas.diminuir(v))}')
