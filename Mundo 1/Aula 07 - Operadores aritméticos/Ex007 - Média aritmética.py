nota1 = float(input('\033[1;31;40mQual foi a sua nota na prova 1? \033[0m'))
nota2 = float(input('\033[1;31;40mQual foi a sua nota na prova 2? \033[0m'))
media = float((nota1 + nota2)/2)
print('\033[1;32;40mA sua media nas provas foi: {}\033[0m'.format(media))
