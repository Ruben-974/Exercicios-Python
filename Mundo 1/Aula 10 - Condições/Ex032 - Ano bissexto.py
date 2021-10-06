from datetime import date
a = int(input('Qual ano você deseja analizar? Digite 0 para analizar o ano atual: '))
if a == 0:
    a = date.today().year
if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
    print('O ano ({}) que você escolheu e um ano bissexto!'.format(a))
else:
    print('O ano ({}) que você escolheu não e um ano bissexto!'.format(a))
