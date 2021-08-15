# : Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.
from math import hypot
cateto_op = float(input('Informe o cateto oposto '))
cateto_adj = float(input('Informe o cateto adjacente '))
hipotenusa = hypot(cateto_op,cateto_adj)
print('Hipotenusa: {:.2f}'.format(hipotenusa))
