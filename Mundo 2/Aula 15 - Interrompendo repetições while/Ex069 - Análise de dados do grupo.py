idade = mais18 = homens = mulhres = 0
while True:
    print('-' * 20)
    print('CADASTRE UMA PESSOA')
    print('-' * 20)
    idade = int(input('Idade: '))
    sexo = continuar = ' '
    while sexo not in 'FM':
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    while continuar not in 'SN':
        print('-' * 28)
        continuar = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    if idade > 18:
        mais18 += 1
    if sexo in 'M':
        homens += 1
    if sexo in 'F' and idade < 20:
        mulhres += 1
    if continuar in 'N':
        break
print('-' * 28)
print(f'''Total de pessoas com mais 18 anos: {mais18}
Ao todo temos {homens} homens cadastrado
E temos {mulhres} mulhres com menos de 20 anos''')
