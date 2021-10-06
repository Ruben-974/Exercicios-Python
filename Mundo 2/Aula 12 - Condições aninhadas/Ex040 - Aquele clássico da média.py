n1 = float(input('Diga a primeira nota: '))
n2 = float(input('Diga a segunda nota: '))
media = (n1 + n2) / 2
if media < 5:
    print('A media de {:.1f} com {:.1f} é {:.1f}'.format(n1, n2, media))
    print('Você esta REPROVADO! deveria ter tido a media maior ou igual a 7, ESTUDE MAIS!')
elif 5 < media < 7:
    print('A media de {:.1f} com {:.1f} é {:.1f}'.format(n1, n2, media))
    print('Você esta de RECUPERAÇÂO, você deveria ter tido a media maior ou igual a 7, ESTUDE MAIS!')
elif media >= 7:
    print('A media de {:.1f} com {:.1f} é {:.1f}'.format(n1, n2, media))
    print('Você esta APROVADO, PARABENS!')
