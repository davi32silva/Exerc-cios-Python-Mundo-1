from math import radians, sin, cos, tan
angulo = float(input('Digite o Ângulo: '))
seno = sin(radians(angulo))
print('O ângulo {} tem o seno de {:.2f}'.format(angulo, seno))
cos = cos(radians(angulo))
print('O ângulo {} tem o cossendo de {:.2f}'.format(angulo, cos))
tan = tan(radians(angulo))
print('O ângulo {} tem a tangente de {:.2f}'.format(angulo, tan))
