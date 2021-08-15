# Crie um programa que faça o computador jogar Jokenpô com você.

from random import randint
print('================================')
print('          JO KEN PO ')
print('================================')

jogo = ('PEDRA', 'TESOURA', 'PAPEL',)

jogadorPC = randint(0,2)

jogador = int(input('''
Faça sua escolha:

    [0] PEDRA
    [1] TESOURA
    [2] PAPEL  
'''))

if jogador == 0:         #pedra
    if jogadorPC == 0:
        print('Empate')
    elif jogadorPC == 1:
        print('Ganhou')
    elif jogadorPC == 2:
        print('Perdeu')
elif jogador == 1:         #tesoura
    if jogadorPC == 1:
        print('Empate')
    elif jogadorPC ==  2:
        print('Ganhou')
    elif jogadorPC == 0:
        print('Perdeu!')
elif jogador == 2:         #papel
    if jogadorPC == 2:
        print('Empate')
    elif jogadorPC == 0:
        print('Ganhou')
    elif jogadorPC == 1:
        print('Perdeu')

print('Computador jogou : {}'.format(jogo[jogadorPC]))
