#
# Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
#
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
#
# Seu programa deverá realizar a operação solicitada em cada caso.

from time import sleep

# lendo dois valores
prim = int(input('Digite um número '))
seg = int(input('Digite outro número '))

op = 0
while op != 5:
    print('----' * 5)
    print('[ 1 ] somar ')
    print('[ 2 ] multiplicar')
    print('[ 3 ] maior')
    print('[ 4 ] novos números')
    print('[ 5 ] sair do programa')
    op = int(input())
    
    if op == 5:
        print('...s a i n d o   d o   s i s t e m a ...')
        sleep(4)
        break
    elif op == 1:
        print('{} + {}  = {}'.format(prim, seg, prim + seg))
        sleep(3)
    elif op == 2:
        print('{} * {} = {} '.format(prim, seg, prim * seg))
        sleep(3)
    elif op == 3:
        if prim > seg:
            print('{} é maior que {}'.format(prim, seg))
            sleep(3)
        elif seg > prim:
            print('{} não é maior que {}'.format(prim, seg))
            sleep(3)
        else:
            print('Os dois números digitados são iguais')
            sleep(3)
    elif op == 4:
        print('-- Digitar novos números --')
        prim = int(input('Digite um número '))
        seg = int(input('Digite outro número '))
    else:
        print('Opção Inválida')
        
print('saiu')
