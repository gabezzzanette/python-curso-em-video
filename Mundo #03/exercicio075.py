# Exercício Python 075: Desenvolva um programa
# que leia quatro valores pelo teclado e guarde-os
# em uma tupla. No final, mostre:
#
# A) Quantas vezes apareceu o valor 9.
#
# B) Em que posição foi digitado o primeiro valor 3.
#
# C) Quais foram os números pares.


numeros = (int(input("Digite numero inteiro: ")), int(input("Digite numero inteiro: ")),
           int(input("Digite numero inteiro: ")), int(input("Digite numero inteiro: ")))

print(f"O valor 9 aparece {numeros.count(9)} vezes.")

if 3 in numeros:
    print(f"O número 3 foi digitado na posição {numeros.index(3)+ 1}º")
else:
    print("O número 3 não foi digitado.")
    
print("Números pares digitados: ")
for n in numeros:
    if n % 2 == 0:
        print(n, end=' ')
