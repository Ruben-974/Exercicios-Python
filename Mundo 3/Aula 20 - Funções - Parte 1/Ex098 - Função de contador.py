from time import sleep


def contar(inicio, fim, passo):
    cont = inicio
    if passo < 0:
        passo = -passo
    if passo == 0:
        passo = 1
    print('/-' * 20 + '/')
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    if inicio < fim:
        while cont <= fim:
            print(cont, end=' ')
            sleep(0.5)
            cont += passo
    else:
        while cont >= fim:
            print(cont, end=' ')
            sleep(0.5)
            cont -= passo
    print('FIM')


contar(0, 10, 1)
contar(10, 0, 2)
print('/-' * 20 + '/')
print('Agora você ira personalizar a contagem!')
contar(int(input('Inicio: ')), int(input('Fim: ')), int(input('Passo: ')))
print('-+- PROGRAMA FINALIZADO -+-')
