#  Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500.
soma = 0
contador = 0
for numero in range (1 , 501,2):
    if numero % 3 == 0:
        contador += 1
        print('O número {} '.format(numero))
        print('e sua soma {} + {} = '.format(soma, numero), end='')
        soma =  numero + soma
print(soma)
print('Tem {} números entre 1 e  500 e multiplos de 3'. format(contador))
