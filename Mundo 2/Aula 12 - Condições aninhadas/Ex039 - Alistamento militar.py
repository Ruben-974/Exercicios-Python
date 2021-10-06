from datetime import date
ano = int(input('Qual e o seu ano de nascimento? '))
idade = date.today().year - ano
print('Quem nasceu em {} está com {} anos, no ano de {}'.format(ano, idade, date.today().year))
if idade == 18:
    print('Você deve se alistar para o exercito esse ano!')
elif idade > 18:
    print('Você ja deveria ter se alistado em {}, a {} anos.'.format(date.today().year - (idade - 18), idade - 18))
elif idade < 18:
    print('Você deverá se alistar em {}, daqui a {} anos.'.format(18 - idade + date.today().year, 18 - idade))
