# O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos. Faça
# um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
from random import shuffle
alunos = ['Ana', 'Gabe', 'João', 'Mario', 'Silva', 'Gustavo', 'Philipe', 'Carla']
#embaralhar os nomes
shuffle(alunos)
print('A ordem de apresentação será: {}'.format(alunos))