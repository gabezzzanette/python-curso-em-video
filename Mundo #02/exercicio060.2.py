#
# Exercício Python 060: Faça um programa que
# leia um número qualquer e mostre o seu fatorial.
# Exemplo:
# 5! = 5 x 4 x 3 x 2 x 1 = 120
#
# usando biblioteca math

from math import factorial

n = int(input('Digite um número para calcular seu Fatorial: '))
f = factorial(n)
print('O fatorial de {} é {}'.format(n,f))
