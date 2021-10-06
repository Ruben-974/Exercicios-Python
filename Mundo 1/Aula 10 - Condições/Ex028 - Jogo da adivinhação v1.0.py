from random import randrange
from time import sleep
n = randrange(5)
print('Pensei em um número de 0 a 5, tente adivinha-lo!')
n1 = int(input('Digite o número: '))
print('PROCESSANDO...')
sleep(2.5)
if n1 == n:
    print('Parabéns, você acertou o número!')
else:
    print('Você não conseguiu, o número era {}, tente novamente!'.format(n))
