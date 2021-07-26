# Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que
# tipo de triângulo será formado:
#
# – EQUILÁTERO: todos os lados iguais
#
# – ISÓSCELES: dois lados iguais, um diferente
#
# – ESCALENO: todos os lados diferentes

reta1 = float(input('Reta [1] :'))
reta2 = float(input('Reta [2] :'))
reta3 = float(input('Reta [3] :'))

if reta2 + reta3 > reta1 and reta2 + reta1 > reta3 and reta3 + reta1 >  reta2:
    print('Formam um triangulo ')
    if reta1 == reta2 ==reta3:
        print('Equilátero')
    elif reta1 != reta2 != reta3:
        print('Escaleno')
    else:
        print('Esósceles')
else:
    print('Não forma um triangulo')