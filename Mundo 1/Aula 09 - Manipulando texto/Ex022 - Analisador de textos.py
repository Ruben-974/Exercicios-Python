nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando o seu nome...')
print('Seu nome em letras maiusculas é: {}'.format(nome.upper()))
print('Seu nome em letras minusculas é: {}'.format(nome.lower()))
print('Seu nome ao todo tem {} letras'.format(len(nome) - nome.count(' ')))
print('Seu Primeiro nome tem {} letras'.format(nome.find(' ')))
