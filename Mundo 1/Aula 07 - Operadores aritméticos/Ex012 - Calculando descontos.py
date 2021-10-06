produto = float(input('Qual o preço do produto? R$ '))
desconto = float(produto-(produto*5/100))
print('Esse produdo de {} reais, com o desconto de 5%, ira ficar no valor de {:.2f} reais!'.format(produto, desconto))
