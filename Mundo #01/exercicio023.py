# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

num = int(input('Digite um numero entre 0 e 9999 : '))
print('Unidade é: {} '.format(num // 1 % 10))
print('Dezena é: {}'.format(num //10 % 10))
print('Centena é: {}'.format(num // 100 % 10))
print('Milhar é: {}'.format(num// 1000 % 10))
