#--------------------------------------------------------------------
# Exercício Python 58: Melhore o jogo do DESAFIO 28
# onde o computador vai “pensar” em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar,
# mostrando no final quantos palpites foram necessários para vencer.
#--------------------------------------------------------------------
# 28.  Escreva um programa que faça o computador “pensar” em um
# número inteiro entre 0 e 5 e peça para o usuário tentar
# descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.-1]))
#--------------------------------------------------------------------

from random import randint
cont = 0
num = randint(0,10)
jogador = False
while not jogador:
    cont += 1
    numJogador = int(input('Adivinhe o número.\nDê seu palpite :'))
    if numJogador != num:
        print('Errou!! Tente novamente ')
    else:
        print('Computador escolheu número : {} '.format(num))
        print('Acertou! Parabéns!')
        jogador = True

print('Foram feitas {} tentativas para adivinhar o número correto.'.format(cont))
