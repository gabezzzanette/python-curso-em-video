# Escreva um programa que faça o computador “pensar” em um
# número inteiro entre 0 e 5 e peça para o usuário tentar
# descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.-1]))

from random import randint

num = randint(0,5)
num_escolhido = int(input('Escolha um número entre 0 e 5 '))
if num_escolhido == num:

    print('Parabéns!!\nVocê acertou o número!')
else:
    print('Errou!\nO número escolhido era {} '.format(num))
    print('Talvez da próxima tenha mais sorte :D ')
