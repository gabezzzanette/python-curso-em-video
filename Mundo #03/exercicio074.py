# Exercício Python 074: Crie um programa que vai
# gerar cinco números aleatórios e colocar em uma tupla.
# Depois disso, mostre a listagem de números gerados e
# também indique o menor e o maior valor que estão na tupla

import random

randomNum = [random.randint(0, 100), random.randint(0, 100),
             random.randint(0, 100), random.randint(0, 100),
             random.randint(0, 100)]

print(f"Números aleatórios: {randomNum}")
print(f"Maior valor  --- {max(randomNum)}")
print(f"Menor valor  --- {min(randomNum)}")
