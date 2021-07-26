# Exercício Python 51: Desenvolva um programa que
# leia o primeiro termo e a razao de uma PA.
# No final, mostre os 10 primeiros termos dessa progressão.

primeiro_termo = int(input('Digite o primeiro termo da Progressão Aritmética  '))
razao = int(input("Digite a razao da PA  "))
decimo = primeiro_termo + (10 - 1) * razao

# decimo + 1, porque o sinal é aberto no - stop do range()-
for x in range(primeiro_termo, decimo + 1, razao):
    print(x, end=' ⇾ ')

print("FIM")
