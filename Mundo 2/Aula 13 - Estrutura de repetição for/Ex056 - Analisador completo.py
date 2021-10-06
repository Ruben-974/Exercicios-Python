media = 0
ihv = 0
nv = 0
mn = 0
for c in range(1, 5):
    print('----- {}ª PESSOA -----'.format(c))
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper()
    media += idade
    if c == 1 and sexo == 'M':
        ihv = idade
        nv = nome
    if sexo == 'M' and idade > ihv:
        ihv = idade
        nv = nome
    if sexo == 'F' and idade < 20:
        mn += 1
print(mn)
print(ihv, nv)