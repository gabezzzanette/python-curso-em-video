#
# Exercício Python 61: Refaça o DESAFIO 51,
# lendo o primeiro termo e a razao de uma PA,
# mostrando os 10 primeiros termos da progressão usando
# a estrutura while.

print('-------- Progressão Aritmética --------')
p_termo = int(input('Primeiro termo: '))
razao = int(input('Razão : '))
decimo = p_termo + (10 - 1) * razao
cont = 1
while cont <= 10:
    print('{} '.format(p_termo))
    p_termo += razao
    cont += 1
