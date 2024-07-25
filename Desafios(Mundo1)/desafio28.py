from random import randint
print('=========Jogo de Advinhação==========')
num = randint(0, 5)
print('Vou pensar um número entre 0 e 5. Você consegue advinhar qual é?')
print('Pensando...')
player = int(input('Em qual número estou pensando nesse momento? '))
if num == player:
    print('PARABÉNS! VOCÊ GANHOU')
else:
    print('Você perdeu! Na verdade, eu pensei no número {}'.format(num))
