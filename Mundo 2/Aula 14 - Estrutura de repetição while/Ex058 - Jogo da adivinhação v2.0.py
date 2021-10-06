from random import randint
print('''\033[1;32mPensei em um número de 0 a 10!
      Tente adivinha-lo\033[0m''')
c = randint(0, 10)
t = 0
p = -1
while c != p:
    p = int(input('Qual número você acha que é? '))
    if c > p:
        print('O número e \033[1;32mMAIOR\033[0m... Tente novamente: ')
    if c < p:
        print('O número e \033[1;31mMENOR\033[0m... Tente novamente: ')
    t += 1
print('O \033[1;34mNÚMERO\033[0m ERA \033[1;33m{}\033[0m! E VOCÊ VENCEU COM \033[1;31m{}\033[0m TENTATIVAS!'.format(c, t))
