# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

nome = str(input('Nome Completo: ')).strip()
print('Nome completo: {}'.format(nome))
nomeList = nome.split()
print('Primeiro nome: {}'.format(nomeList[0]))
print('Ultimo nome: {}'.format(nomeList[len(nomeList)-1]))