#
# Exercício Python 67: Faça um programa
# que mostre a tabuada de vários números,
# um de cada vez, para cada valor digitado
# pelo usuário. O programa será interrompido
# quando o número solicitado for negativo.
#

print('* = *' * 7)
print('\t\t\tTabuada')
print('* = *' * 7)

# loop infinito com número negativo como saída
while True:
    numTab = int(input('Digite o número da tabuada que deseja ver '))
    if numTab < 0:
        print('---' * 10)
        print('Número digitado é NEGATIVO')
        print('Fim do programa de Tabuada')
        break
    print('---' * 10)
    for count in range(1, 11):
        result = numTab * count
        print(f'\t{numTab} x {count} = {result}')
        
    print('---' * 10)
