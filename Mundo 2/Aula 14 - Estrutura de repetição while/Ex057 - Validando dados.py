s = str(input('Informe o seu sexo [M/F]: ')).strip().upper()[0]
while s not in 'FM':
    s = str(input('Opção invalida! Informe o seu sexo [M/F]: ')).strip().upper()[0]
print('O sexo {} foi registrado com sucesso!'.format(s))
