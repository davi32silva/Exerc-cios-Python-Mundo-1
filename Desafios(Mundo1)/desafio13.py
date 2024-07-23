print('============Mecânica============')
print('       Reajuste de Salário      ')
print('================================')
nome = str(input('NOME DO FUNCIONÁRIO: '))
salario = float(input('SALÁRIO DO FUNCIONÁRIO: '))
reajuste = (salario*0.15)+salario
print('Com o reajuste de salário de R${} em 15%, \no funcionário {} vai receber R${}'.format(salario, nome, reajuste))
