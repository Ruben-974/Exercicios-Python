def voto(nascimento):
    from datetime import date
    ano = date.today().year
    idade = ano - nascimento
    if idade < 16:
        return print(f'A pessoa com {idade} anos NÃO TEM DIREITO AO VOTO!')
    elif 16 <= idade < 18 or idade > 70:
        return print(f'A pessoa com {idade} anos TEM O VOTO OPCIONAL!')
    else:
        return print(f'A pessoa com {idade} anos TEM O VOTO OBRIGATORIO!')


voto(int(input('Qual o seu ano de nascimento? ')))
