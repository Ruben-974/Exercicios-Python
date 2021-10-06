from random import choice
print('Um professor quer sortear um aluno para apgar o quadro, site 5')
nome1 = input('Aluno 1: ')
nome2 = input('Aluno 2: ')
nome3 = input('Aluno 3: ')
nome4 = input('Aluno 4: ')
nome5 = input('Aluno 5: ')
s = choice([nome1, nome2, nome3, nome4, nome5])
print('O aluno sortiado foi: {}'.format(s))
