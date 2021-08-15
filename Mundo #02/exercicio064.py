#
# Exercício Python 64: Crie um programa
# que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar
# o valor 999, que é a condição de parada. No final,
# mostre quantos números foram digitados e qual foi a
# soma entre eles (desconsiderando o flag).
#
cont = num = total = 0

print('===' * 10)
print('Digite números inteiros -[ 999 ]  para parar ')

while num != 999:
    
    num = int(input())
    total += num
    cont += 1


total -= 999
cont -= 1
print('Foram digitados {} números somando ao total {}'.format(cont, total))
