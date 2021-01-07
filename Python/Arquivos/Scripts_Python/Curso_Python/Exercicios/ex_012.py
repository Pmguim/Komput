print('Olá humano!')

Preço = float(input('Qualé o preço do produto? R$ '))
Desc = int(input('Qual e o valor a ser descontado? '))

Quoc = Preço - (Preço*Desc/100)

print('O preço do produto, descontando {}%, é R${:.2f}.'.format(Desc, Quoc))
