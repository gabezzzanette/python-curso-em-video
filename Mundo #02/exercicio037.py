# Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.
#ler numero inteiro qualquer
numero = int(input('Digite um número para conversão : '))
print('[1] - Binário')
print('[2] - Octal')
print('[3] - Hexadecimal')
opcao = int(input('Conversão numero: '))

if opcao == 1:
    print(' [ {} ] em binario >>> [ {} ]'.format(numero,bin(numero)[2:]))
elif opcao == 2:
    print(' [ {} ] em octal >>> [ {} ]'.format(numero, oct(numero)[2:]))
elif opcao == 3:
    print(' [ {} ] em hexadecimal >>> [ {} ]'.format(numero, hex(numero)[2:]))
else:
    print('Operação não encontrada!')
