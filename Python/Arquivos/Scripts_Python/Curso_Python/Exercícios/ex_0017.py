from math import hypot

print('Olá humano!')

a = float(input('Insira o comprimento do cateto oposto : '))
b = float(input('Insira o comprimento do cateto adjacente: '))
    
hip = hypot(a, b)

print('A hipotenusa dos  catetos {} e {}, é {:.2f}.'.format(a, b, hip))
