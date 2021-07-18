# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo

reta1 = float(input('Reta [1] :'))
reta2 = float(input('Reta [2] :'))
reta3 = float(input('Reta [3] :'))

if reta2 + reta3 > reta1 and reta2 + reta1 > reta3 and reta3 + reta1 >  reta2:
    print('As retas lidas formam um triangulo!')
else:
    print('As retas lidas não formam um triangulo')