# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira
from math import trunc
num = float(input('Digite um numero Real '))
print('O número digitado foi {} e sua parte inteira é {}'.format(num, trunc(num)))
print('(sem importar math) \nnúmero digitado {}e sua parte inteira é {}'.format(num,int(num)))
