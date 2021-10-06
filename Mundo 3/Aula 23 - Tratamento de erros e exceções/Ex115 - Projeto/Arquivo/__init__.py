def ExisteArquivo(nome):
    try:
        arquivo = open(nome, 'rt')
        arquivo.close()
    except:
        print(f'O arquivo "{nome}" não foi encontrado!')
        return True
    else:
        return False


def CriarArquivo(nome):
    try:
        arquivo = open(nome, 'wt+')
    except:
        print(f'ERRO: Não foi possivel criar o arquivo "{nome}"')
    else:

        return arquivo


def LerArquivo(nome):
    try:
        arquivo = open(nome, 'rt')
    except:
        print(f'ERRO: Não foi possivel ler o arquivo "{nome}"')
    else:
        print(arquivo.read())

