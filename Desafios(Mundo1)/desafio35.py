c1 = int(input('Digite o Primeiro Comprimento: '))
c2 = int(input('Digite o Segundo Comprimento: '))
c3 = int(input('Digite o Terceiro Comprimento: '))
#TRIÂNGULO EQUILÁTERO:
if c1 == c2 and c2 == c3 and c3 == c1:
    print('O triângulo formado com os valores {}, {} e {} é um TRIÂNGULO EQUILÁTERO'.format(c1, c2, c3))
#TRIÂNGULO ISÓSCELES:
if c1 == c2 and c2 == c1 and c3 != c1:
    print('O triângulo formado com os valores {}, {} e {} é um TRIÂNGULO ISÓSCELES'.format(c1, c2, c3))
elif c2 != c1 and c2 == c3 and c3 == c2:
    print('O triângulo formado com os valores {}, {} e {} é um TRIÂNGULO ISÓSCELES'.format(c1, c2, c3))
elif c1 == c3 and c2 != c3 and c3 == c1:
    print('O triângulo formado com os valores {}, {} e {} é um TRIÂNGULO ISÓSCELES'.format(c1, c2, c3))
#TRIÂNGULO ESCALENO:
if c1 != c2 and c2 != c3 and c3 != c1:
    print('O triângulo formado com os valores {}, {} e {} é um TRIÂNGULO ESCALENO'.format(c1, c2, c3))


