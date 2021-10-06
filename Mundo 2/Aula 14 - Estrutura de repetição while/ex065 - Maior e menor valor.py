n = media = cont = soma = maior = menor = 0
ns = 'S'
while ns not in 'N':
    n = int(input('Digite um número: '))
    ns = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    cont += 1
    soma += n
    if cont == 1:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
print('Você digitou {} números e a media foi {:.2f}\nO maior valor foi {} e o menor valor foi {}'.format(cont, soma / cont, maior, menor))
