#
# Exercício Python 65: Crie um programa que leia vários
# números inteiros pelo teclado. No final da execução
# mostre a média entre todos os valores e qual foi o
# maior e o menor valores lidos. O programa deve perguntar
# ao usuário se ele quer ou não continuar a digitar valores.

op = False
cont = total = 0
maior = menor = 0

print('---' * 10)

while not op:
    
    num = int(input("Digite um número: "))
    total += num
    cont += 1
    op2 = str(input('Deseja terminar o programa? "S/N" '))
    
    if cont == 1:
        maior = menor = num
    if op2 in 'Ss':
        op = True
        print('saindo...')
        
    if num > maior:
        maior = num
    elif num < menor:
        menor = num
        
media = total / cont

print('Foram digitados {} números'.format(cont))
print('A média dos números foi {}'.format(media))
print('Sendo o número {} o maior entre eles e o número {} o menor'.format(maior, menor))
