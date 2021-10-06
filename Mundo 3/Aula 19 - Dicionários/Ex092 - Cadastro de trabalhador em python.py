from datetime import date
ano = date.today().year
pessoa = {'nome': str(input('Nome: ')).capitalize(), 'idade': ano - (int(input('Ano de nascimento: '))),
          'ctps': int(input('Carteira de Trabalho [0 não tem]: '))}
if pessoa['ctps'] != 0:
    pessoa['contratação'] = int(input('Ano de contratação: '))
    pessoa['salario'] = float(input('Salário R$'))
    pessoa['aposentadoria'] = (35 - (ano - pessoa['contratação']) + pessoa['idade'])
print('<>' * 20)
for k, v in pessoa.items():
    print(f'    - {k.capitalize()} corresponde à {v}')
print('<>' * 20)
