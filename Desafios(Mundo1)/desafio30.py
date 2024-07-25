n = int(input('Digite um número: '))
imparpar = n % 2
if imparpar == 0:
    print('O número {} é par'.format(n))
else:
    print('O número {} é ímpar'.format(n))
