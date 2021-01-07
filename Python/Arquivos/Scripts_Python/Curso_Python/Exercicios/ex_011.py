print('Olá humano!')

Larg = float(input('Insira a medida de largura: '))
Alt = float(input('Insira a medida da altura: '))
Área = Larg * Alt

print('Sua parede tem a dimensão de {} x {} e uma área de {}m².'.format(Larg, Alt, Área))
Tinta = Área / 2
print('Para pintar esta parede, serão necessários {}l de tinta.'.format(Tinta))
