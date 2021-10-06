def frase(txt):
    caracteres = len(txt)+4
    print('-' * caracteres)
    print(f'{txt:^{caracteres}}')
    print('-' * caracteres)


cont = int(input('Quantas frases você quer digitar? '))
for c in range(0, cont):
    frase(str(input(f'Digite a {c + 1}° Frase / Palavra: ')).strip())
print()
print('--:-- FINALIZADO --:--')
