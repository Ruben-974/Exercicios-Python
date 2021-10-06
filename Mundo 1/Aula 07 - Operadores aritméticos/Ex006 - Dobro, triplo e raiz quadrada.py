n = int(input('Digite um número: '))
print('O\033[34;1m dobro\033[0m do {} é {}\nO \033[35;1mtriblo\033[0m de {} é {}\nA \033[36;1mraiz quadrada\033[0m de {} é {:.2f}'.format(n, (n*2), n, (n*3), n, pow(n, (1/2))))
