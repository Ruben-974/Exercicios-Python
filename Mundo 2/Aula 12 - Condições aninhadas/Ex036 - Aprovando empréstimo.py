casa = float(input('Qual o valor da casa que você deseja comprar? '))
sal = float(input('Qual e o seu salario? '))
par = float(input('Em quantos anos você deseja pagar? '))
par2 = par * 12
div = casa / par2
sal2 = sal * 30 / 100
if sal2 >= div:
    print('O imprestimo para comprar a casa foi aprovado! A parcela sera de R${:.2f} mensais'.format(div))
else:
    print('O imprestimo foi negado, pois \033[1;32mR${:.2f}\033[0m mensais esta excedendo 30% do seu salario'.format(div))
