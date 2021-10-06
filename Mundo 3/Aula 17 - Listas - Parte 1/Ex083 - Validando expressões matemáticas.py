print('VALIDAR EXPRESSÃO!')
expre = str(input('Digite uma expreção: '))
cont1 = cont2 = 0
for e in expre:
    if e == '(':
        cont1 += 1
    if e == ')':
        cont2 += 1
if cont1 == cont2:
    print('A expressão e valida!')
if cont1 != cont2:
    print('A expressão não e valida!')