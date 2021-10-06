aluno = {'nome': str(input('Nome: ')).capitalize()}
aluno['media'] = float(input(f'Média de {aluno["nome"]}: '))
if aluno['media'] >= 7:
    aluno['situaçao'] = 'aprovado'
elif 5 < aluno['media'] < 7:
    aluno['situaçao'] = 'recuperação'
elif aluno['media'] < 5:
    aluno['situaçao'] = 'reprovado'
print('<>' * 18)
for k, v in aluno.items():
    print(f'{k} é igual a {v}')
print('<>' * 18)
