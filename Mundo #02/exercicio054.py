# Exercício Python 54: Crie um programa que leia o
# ano de nascimento de sete pessoas. No final,
# mostre quantas pessoas ainda não atingiram a
# maioridade e quantas já são maiores.

from datetime import date

dataAtual = date.today().year
c_maiorIdade = 0
c_menorIdade = 0
for x in range(0, 7):
    dataNascimento = int(input('Data de Nascimento : '))
    idade = dataAtual - dataNascimento
    if idade >= 18:
        c_maiorIdade += 1
    else:
        c_menorIdade += 1
print('{} pessoas são maiores de idade e {} menores de idade'.format(c_maiorIdade, c_menorIdade))