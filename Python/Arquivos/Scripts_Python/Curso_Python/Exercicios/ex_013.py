print('Olá humano!')

Sal = float(input('Insira o valor do funcionário: '))
Aum = int(input('Insira a porcentagem que será incrementada ao salário: '))

Quoc = Sal + (Sal+Aum/100)

print('O salário do funcionário será aumentado em {}%, e passará'.format(Aum))
print('de R${} para R${:.2f}'.format(Sal, Quoc))
