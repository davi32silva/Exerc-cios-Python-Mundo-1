from math import hypot
co = float(input('Digite o comprimento do Cateto Oposto: '))
ca = float(input('Digite o comprimento do Cateto Adjacente: '))
hi = hypot(co, ca)
print('Com a soma dos catetos {} e {}, a hipotenusa vai medir {:.2f}'.format(co, ca, hi))
