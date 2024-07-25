from datetime import date
print('--------------------------')
print(' ANÁLISE DE ANO BISSEXTO  ')
print('--------------------------')
ano = int(input('Que ano você quer analisar? (Aperte [0] para verificaro ano atual)'))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0:
    print('O ano {} é bissexto.'.format(ano))
else:
    print('O ano {} não é bissexto.'.format(ano))
