from Interface import *
from Arquivo import *

existe = ExisteArquivo('ListaPessoas.txt')
if existe:
    arquivo = CriarArquivo('ListaPessoas.txt')
while True:
    res = int(opções(['Lista de Pessoas', 'Cadastrar Pessoa', 'Sair do Programa']))
    if res == 1:
        titulo('~-~ OPÇÃO 1 ~-~', cor=33, formato=1)
        LerArquivo('ListaPessoas.txt')
    if res == 2:
        titulo('~-~ OPÇÃO 2 ~-~', cor=33, formato=1)
        nome = input('Nome: ')
        idade = input('Idade: ')
    if res == 3:
        titulo('SAINDO DO PROGRAMA...', cor=33, formato=1)
        break
