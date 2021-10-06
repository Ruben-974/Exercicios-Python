resposta = ' '
ver = 0
aluno = []
notas = []
alunos = []
while resposta not in 'N':
    resposta = ' '
    aluno.append(str(input('Nome: ')).capitalize())
    notas.append(float(input('Nota 1: ')))
    notas.append(float(input('Nota 2: ')))
    aluno.append(notas[:])
    alunos.append(aluno[:])
    aluno.clear()
    notas.clear()
    while resposta not in 'NS':
        resposta = str(input('Cadastrar novos alunos? [S/N]: ')).upper().strip()
print('<>' * 17)
print('N°. Nome.        Média')
print('<>' * 17)
for c in range(len(alunos)):
    print(f'{c}   {alunos[c][0]:<10} {((alunos[c][1][0] + alunos[c][1][1]) / 2):>7}')
print('<>' * 28)
while True:
    ver = int(input('Mostrar notas de qual aluno? [999 PARA INTERROMPER]: '))
    if ver == 999:
        break
    print(f'As notas de {alunos[ver][0]} são: {alunos[ver][1]}')
print('Programa Finalizado!')