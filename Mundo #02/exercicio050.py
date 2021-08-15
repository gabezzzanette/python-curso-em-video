 # Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
 # Se o valor digitado for ímpar, desconsidere-o.

print('====***===' *2)
soma = 0
count= 0
for numero in range(1, 7):
     num = int(input('Digite o {}º numero :  '.format(numero)))
     if num % 2 == 0:
        soma += num
        count += 1
print('A soma dos pares foi: {}'.format(soma))
print('{} numeros foram lidos'.format(count))
