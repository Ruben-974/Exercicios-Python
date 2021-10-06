from datetime import date
nas = int(input('Qual e o seu ano de nascimento? '))
ano = date.today().year
idade = ano - nas
print('O atleta tem {} anos.'.format(idade))
if idade <= 9:
    print('Classificado: MIRIM.')
elif idade <= 14:
    print('Classificado: INFANTIL.')
elif idade <= 20:
    print('Classificado: JUNIOR.')
elif idade <= 25:
    print('Classificado: SÊNIOR.')
elif idade > 25:
    print('Classificado: MASTER.')
