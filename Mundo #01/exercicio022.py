# Crie um programa que leia o nome completo de uma pessoa e mostre:
#
# – O nome com todas as letras maiúsculas e minúsculas.
#
# – Quantas letras ao todo (sem considerar espaços).
#
# – Quantas letras tem o primeiro nome.

nome_comp = input('Digite seu nome completo: ')
print('O nome {} tem '.format(nome_comp.upper()))
# print('O nome {} tem '.format(nome_comp.lower()))
print('Possui {} letras '.format(len(nome_comp.replace(" ",""))))
print('O primeiro nome possui {} letras'.format(len(nome_comp.split()[0])))