from random import shuffle
print('Um professor quer fazer um sorteio para decidir qual será a ordem para apresentar os trabalhos, cite o nome de 5 alunos: ')
n1 = input('Aluno 1: ')
n2 = input('Aluno 2: ')
n3 = input('Aluno 3: ')
n4 = input('Aluno 4: ')
n5 = input('Aluno 5: ')
lista = [n1, n2, n3, n4, n5]
shuffle(lista)
print('A sequencia de alunos será:\n{}'.format(lista))
