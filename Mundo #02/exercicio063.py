#
# Exercício Python 63: Escreva um programa
# que leia um número N inteiro qualquer e
# mostre na tela os N primeiros elementos de
# uma Sequência de Fibonacci. Exemplo:
#
# 0 – 1 – 1 – 2 – 3 – 5 – 8
#

pNumeros = int(input('Mostrar na tela quantos elemetos da Sequência de Fibonacci? '))
cont = 1
atual = 1
anterior = 0
while cont <= pNumeros:
    
    print('{}'.format(anterior), end='')
    print(' - ' if cont < pNumeros else ' ', end='')
    result = anterior + atual
    anterior = atual
    atual = result
    cont += 1

print('\nFibonacci de {} sequências '.format(cont-1))




