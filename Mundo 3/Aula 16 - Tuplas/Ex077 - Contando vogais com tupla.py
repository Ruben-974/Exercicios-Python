palavras = ('Teste', 'Python', 'Estudo', 'Algoritimo')
for c in palavras:
    print(f'\nNa palavra {c.upper()} Temos ... ', end='')
    for letra in c:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')












