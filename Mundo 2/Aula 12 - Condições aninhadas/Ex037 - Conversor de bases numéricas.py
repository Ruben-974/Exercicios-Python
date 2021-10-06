num = int(input('Digite um número inteiro para ser convertido: '))
print('''Escolha uma opção de conversão
 [ 1 ] Para converter para BINARIO
 [ 2 ] Para converter para OCTAL
 [ 3 ] Para converter para HEXADECIMAL''')
opç = int(input('Escolha uma das opções: '))
if opç == 1:
    print('O valor {} convertido para BINARIO é: {}'.format(num, bin(num)[2:]))
elif opç == 2:
    print('O valor{} convertido para OCTAL é: {}'.format(num, oct(num)[2:]))
elif opç == 3:
    print('O valor {} convertido para HEXADECIMAL é: {}'.format(num, hex(num)[2:]))
else:
    print('OPÇÃO INVALIDA, TENTE NOVAMENTE!')
