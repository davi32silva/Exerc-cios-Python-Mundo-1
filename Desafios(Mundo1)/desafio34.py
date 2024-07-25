print('--------------------------')
print('   REAJUSTE DE SALÁRIO    ')
print('--------------------------')
s = float(input('Digite o salário do funcionário: '))
r1 = s + (s * 0.10)
r2 = s + (s * 0.15)
if s >= 1250:
    print('Com o reajuste desse salário, o salário fica em R${}'.format(r1))
else:
    print('Com o reajuste desse salário, agora o salário fica em R${}'.format(r2))
