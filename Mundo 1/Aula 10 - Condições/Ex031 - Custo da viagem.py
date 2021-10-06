km = float(input('Quantos KM foi a viajem? '))
if km <= 200:
    print('Você percoreu {} e ira pagar R$0,50 por KM! Que no total será: {:.2f}!'.format(km, km*0.40))
else:
    print('Como a viajem foi {}KM sendo maior que 200KM, em vez de pagar R$0,50 por KM, você ira pagar R$0,45 por KM! Totalizando R${:.2f}!'.format(km, km*0.40))