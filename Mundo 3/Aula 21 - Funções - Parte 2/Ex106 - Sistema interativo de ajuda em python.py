def linha(txt, cor='\033[m', traço='-'):
    """
    -> Cria uma Palavra/Frase personalizada
    txt: Recebe o texto que você deseja formatar
    cor: Para escolher a cor e outras formatações
    traço: Um caracter personalizado para cercar o seu texto
    """
    t = 4+len(txt)
    print(f'{cor}{traço}' * t)
    print(f'{txt:^{t}}')
    print(f'{traço}' * t)
    print('\033[m', end='')


def ajuda():
    while True:
        linha('~ SISTEMA DE AJUDA PyHELP ~', '\033[1;33m')
        duvida = str(input('Função da biblioteca: ')).lower()
        linha(f'Acessando o manual do comando {duvida}', '\033[1;35m')
        if duvida != 'fim':
            print('\033[1;34m', end='')
            help(duvida)
            print('\033[m', end='')
        if duvida == 'fim':
            linha('~ SISTESMA FINALIZADO ~', '\033[1;32m')
            
ajuda()