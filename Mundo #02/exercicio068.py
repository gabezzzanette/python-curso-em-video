#
# Exercício Python 68: Faça um programa que
# jogue par ou ímpar com o computador. O jogo
# só será interrompido quando o jogador perder,
# mostrando o total de vitórias consecutivas que
# ele conquistou no final do jogo.
#

from random import randint

print('***' * 13)
print('\t\tJOGO DO PAR OU ÍMPAR')
print('***' * 13)

# loop infinito com jogador perdendo como saída
while True:
    # escolha do jogador
    escolha = int(input('Escolha um número: '))
    parOuImparJogador = str(input('Escolha e escreva: PAR ou IMPAR ?')).strip().upper()
    
    if parOuImparJogador == 'PAR':
        parOuImparJogador = 1
    if parOuImparJogador == 'IMPAR':
        parOuImparJogador = 2
        
    # escolha do computador
    escolhaPC = randint(0,10)
    parOuImparPC = randint(1,2)
    
    if parOuImparPC == 1:
        pc = 'PAR'
    else:
        pc = 'IMPAR'
    
    soma = escolha + escolhaPC
    if soma % 2 == 0:
        resultado = 1
        
    else:
        resultado = 2
        
    if resultado == parOuImparPC and resultado == parOuImparJogador:
        print(f'Empate - PC {escolhaPC} {pc} | Jogador {escolha}')
    elif resultado == parOuImparJogador:
        print(f'Jogador ganhou! - PC {escolhaPC}  {pc}| Jogador {escolha}')
    elif resultado == parOuImparPC:
        print(f'Computador ganhou!! - PC {escolhaPC}  {pc}| Jogador {escolha}')
        break

    print('--*--' * 10)
print('--*--' * 10)
print('Você perdeu, que pena. Tente de novo!')
