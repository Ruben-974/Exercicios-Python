f = str(input('Digite uma frase: ')).upper().split()
junto = ''.join(f)
pa = ''
for c in range(len(junto) -1, -1, -1):
    pa += junto[c]
print('A palavra {}, o inverso {}'.format(junto, pa))
if junto == pa:
    print('Essa e uma frase PALINDROMO')
else:
    print('Essa Não e uma frase PALINDROMO')
