print('-=-=-=-=-=- CALCULAR PA -=-=-=-=-=-')
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
contar = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while contar <= total:
        print(termo, end=' - ')
        termo += razao
        contar += 1
    print('PAUSE')
    mais = int(input('\nDeseja continuar? Digite o valor desejado, se não digite 0: '))
print('')
print('O PROGRAMA FOI FINALIZADO COM {} TERMOS!'.format(total))