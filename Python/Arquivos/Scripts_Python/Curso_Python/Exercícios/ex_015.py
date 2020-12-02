print('Olá humano!')

Dia = int(input('Por quantos dias o veículo foi alugado? '))
Km = float(input('Quantos Km foram rodados com o veículo? '))

Diatot = Dia*60
Kmtot = Km*0.15

Quoc = Kmtot+Diatot

print('\nSomando os valores: \n')
print(Dia, ' x R$60')
print(Km, ' x R$ 0.15')
print('_' * 20)

print('O valor total a ser pago é: R${:.2f}'.format(Quoc))
