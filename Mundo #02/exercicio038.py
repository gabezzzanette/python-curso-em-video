# Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela
# uma mensagem:
#
# – O primeiro valor é maior
#
# – O segundo valor é maior
#
# – Não existe valor maior, os dois são iguais

numero= int(input('Número[1]:  '))
numero2= int(input('Número[2]:  '))

if numero == numero2:
    print('Os números são iguais!')
elif numero > numero2:
    print('O primeiro numero [{}] é maior !'.format(numero))
else:
    print('O segundo numero [{}] é maior !'.format(numero2))
    