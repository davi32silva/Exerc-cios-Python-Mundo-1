km = int(input('Quantos quilometros foram percorridos? '))
multa = (km - 80) * 7  #para não calcular os valores excedentes
if km > 80:
    print('Você foi multado em R${} por ter ultrapassado o limite de 80km/h'.format(multa))
else:
    print('Você não foi multado. Continue assim...')