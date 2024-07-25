print('--------------------------')
print('        PASSAGEM          ')
print('--------------------------')
P = float(input('QUAL A DISTÂNCIA DA VIAGEM? '))
if P <= 200:
    print('O valor da passagem é R${}'.format(P*0.50))
elif P > 200:
    print('O valor da passagem passa dos 200km, então a passagem ficará por R${}'.format(P*0.45))
