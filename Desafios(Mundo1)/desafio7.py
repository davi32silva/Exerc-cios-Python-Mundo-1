nome = str(input('Digite o nome do aluno: '))
N1 = float(input('Digite a primeira nota do aluno: '))
N2 = float(input('Digite a segunda nota do aluno: '))
media = (N1+N2)/2
print('A média do aluno {:.1f} entre as notas {:.1f} e {:.1f} é {:.1f}'.format(nome, N1, N2, media))