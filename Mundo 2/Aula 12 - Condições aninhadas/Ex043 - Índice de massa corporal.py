peso = float(input('Qual o seu peso ? (Kg) '))
altura = float(input('Qual a sua altura? (M) '))
imc = (peso / (altura * altura))
print('O IMC da pessoa é: {:.1f}'.format(imc))
if imc < 18.5:
    print('Você esta abaixo do peso! CUIDADO!')
elif 18.5 <= imc < 25:
    print('Você está no peso ideal! PARABENS!')
elif 25 <= imc < 30:
    print('Você está Sobrepeso! CUIDADO!')
elif 30 <= imc < 40:
    print('Você está na Obesidade! CUIDADO!')
elif imc >= 40:
    print('Você esta na OBESIDADE MÓRBIDA! CUIDADO!')
