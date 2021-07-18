# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar,
# sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.


dias = int(input("Quantos dias foi alugado: "))
km_percorrido = float(input("Quantos km foram rodados: "))
pagar = (dias * 60.0) + (km_percorrido * 0.15)
print("O carro alugado por {} dias e percorrido {}km é : R${}".format(dias,km_percorrido, pagar ))