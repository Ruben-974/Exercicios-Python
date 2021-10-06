n = 0
while True:
    print('-=' * 20)
    n = int(input('Quer ver a tabuada de qual valor? '))
    print('-=' * 20)
    if n < 0:
        break
    for c in range(1, 11):
        print(f'{n} x {c:2} = {c * n}')
print('')
print('PROGRAMA FINALIZADO! :D')
