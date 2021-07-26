# Exercício Python 55: Faça um programa que
# leia o peso de cinco pessoas.
# No final, mostre qual foi o maior e o menor peso lidos.

for x in range(0, 5):
    peso = float(input('Digite seu peso: '))
    if x == 0:
        maior = peso
        menor = peso
    else:
        if peso < menor:
            menor = peso
        if peso > maior:
            maior = peso
print('O maior peso foi {}kg e o menor foi {}kg'.format(maior, menor))



