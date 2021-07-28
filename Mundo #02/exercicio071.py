#
# Exercício Python 071: Crie um programa que simule o funcionamento de um caixa eletrônico.
# No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e
# o programa vai informar quantas cédulas de cada valor serão entregues.
# OBS:
# considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
#

print('''
 +-+-+-+-+-+ +-+-+-+-+-+-+-+-+-+-+
 |C|a|i|x|a| |E|l|e|t|r|o|n|i|c|o|
 +-+-+-+-+-+ +-+-+-+-+-+-+-+-+-+-+
''')

total = sacar = contador = 0
cedula = 50

sacar = int(input('Valor para saque: \n'))
total = sacar

print(f'O valor sacado foi de: {sacar}')

while True:
    
    if total >= cedula:
        total -= cedula
        contador += 1
    else:
        if contador > 0:
            print(f'Entregues {contador} cédulas de {cedula} ')
        
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        
        contador = 0
        
        if total == 0:
            break
