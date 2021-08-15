# Programa que leia um numero e mostre sua raiz quadrada, o dobro e o triplo

num = int(input("Digite um número: "))
print("O número é {}\nSeu dobro é {} e seu triplo é {} \nSua raiz quadrada é {}.".format(num,num*2,num*3, pow(num,1/2)))

