frase = input('Digite uma frase: ')
frase1 = frase.upper()
a = frase1.count('A')
print('Na sua frase aparece {}x a letra "a"!'.format(a))
print('A primeira letra "a" se encontra na posiçâo {}'.format(frase1.find('A')+1))
print('A ultima letra "a" se encontra na posiçâo {}'.format(frase1.rfind('A')+1))