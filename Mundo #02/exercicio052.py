# Exercício Python 52: Faça um programa que leia
# um número inteiro e diga se ele é ou não um número primo.
# numero primo são os aqueles divisiveis por um e por ele mesmo
num = int(input('Digite um número inteiro: '))
cont = 0
for x in range(1, num + 1):
    if num != 0:
        if num % x == 0:
            cont = cont + 1
if cont == 1 or cont > 2:
    print('O número não é primo')
else:
    print('O número é primo!!')
    