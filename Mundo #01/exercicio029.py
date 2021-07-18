# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre
# uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

# ler a velocidade do usuario
velocidade = int(input('Velocidade do carro:  '))

# verificar se a velocidade ultrapassou 80 km
if velocidade > 80:
    print('MULTADO!\nUltrapassou a velocidade permitida!')
    multa = (velocidade - 80) * 7
    print('A multa de R${:.2f} deve ser paga.'.format(multa))
else:
    print('Velocidade permitida, tenha uma boa viagem!')