n1 = int(input('Primeiro Número: '))
n2 = int(input('Segundo Número: '))
n3 = int(input('Terceiro Número: '))
#MENORES:
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
#MAIORES:
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
#Mostra qual número é menor e qual é o maior
print('O menor número é {}'.format(menor))
print('O maior número é {}'.format(maior))
