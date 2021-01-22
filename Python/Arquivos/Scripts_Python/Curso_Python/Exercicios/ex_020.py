import random

print('Olá humano!')

Aluno1 = str(input('Nome do primeiro aluno: '))
Aluno2 = str(input('Nome do segundo aluno: '))
Aluno3 = str(input('Nome do terceiro aluno: '))
Aluno4 = str(input('Nome do quarto aluno: '))

lista = [Aluno1, Aluno2, Aluno3, Aluno4]

random.shuffle(lista)

print('A ordem de apresentação será: ')
print(lista)
