from math import radians, sin, cos, tan
ang = float(input('Digite um ângulo desejado: '))
seno = sin(radians(ang))
cosseno = cos(radians(ang))
tange = tan(radians(ang))
print('O ângulo de {} \ntem o seno de {:.2f}\no cosseno de {:.2f}\ne a tangente de {:.2f}'.format(ang, seno, cosseno, tange))
