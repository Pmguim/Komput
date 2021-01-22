import math

print('Olá humano!')

#ângulo inserido pelo usuário
Ang1 = float(input(('Insira um ângulo: ')))

#Seno do ângulo
Seno = math.sin(math.radians(Ang1))
print('O ângulo de {}, tem o SENO de {:.2f}.'.format(Ang1, Seno))

#Cosseno do ângulo
Cos = math.cos(math.radians(Ang1))
print('O ângulo {}, tem o COSSENO de {:.2F}.'.format(Ang1, Cos))

#Tangente do ângulo
Tan = math.tan(math.radians(Ang1))
print('O ângulo de {}, tem a TANGENTE de {:.2f}.'.format(Ang1, Tan))
