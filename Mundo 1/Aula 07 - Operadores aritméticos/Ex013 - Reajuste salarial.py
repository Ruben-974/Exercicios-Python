salario = float(input('Qual o salário do funcionario? R$ '))
aumento1 = float(salario*15/100)+salario
print('O salario de R${:.2f}, ira receber um aumento de 15%, e ficara no total R${:.2f}!'.format(salario, aumento1))
