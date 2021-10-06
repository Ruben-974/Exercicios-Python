import Moedas

v = int(input('Digite o preço: R$'))
print(f'A metade de {v} é {Moedas.metade(v)}')
print(f'A dobro de {v} é {Moedas.dobro(v)}')
print(f'Aumentando {v} em 10%, temos no total {Moedas.aumentar(v)}')
print(f'Diminuir {v} em 10%, temos no total {Moedas.diminuir(v)}')
