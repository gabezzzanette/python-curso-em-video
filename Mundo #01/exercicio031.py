# Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem,
# cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.format(num))

distancia = float(input('Distancia da viagem: '))
if distancia > 200:
    passagem = 0.45 * distancia
else:
    passagem = 0.5 * distancia
print('Valor da passagem: R${:.2f}'.format(passagem))