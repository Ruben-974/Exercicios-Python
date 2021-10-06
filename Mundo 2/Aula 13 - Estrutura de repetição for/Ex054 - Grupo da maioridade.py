from datetime import date
maior = 0
menor = 0
ano = date.today().year
for c in range(1, 8):
    nasc = int(input('Qual o ano de nascimento da {}ª pessoa: '.format(c)))
    idade = ano - nasc
    if idade >= 21:
        maior += 1
    else:
        menor += 1
print('{} pessoas ja são de maior e {} ainda são de menor'.format(maior, menor))