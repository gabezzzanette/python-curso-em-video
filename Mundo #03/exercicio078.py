# Exercício Python 078: Faça um programa que leia 5 valores
# numéricos e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor
# valor digitado e as suas respectivas posições na lista.

listnumbers = []
smaller = largest = 0

for count in range(0, 5):
    listnumbers.append(int(input(f"[{count + 1}] Digite um numero: ")))
    if count == 0:
        smaller = largest = listnumbers[count]
    else:
        if listnumbers[count] > largest:
            largest = listnumbers[count]
        if listnumbers[count] < smaller:
            smaller = listnumbers[count]

print(listnumbers)

# highest number position
print(f"O maior número na lista foi {largest} nas posições", end=' ')
for i, number in enumerate(listnumbers, start=1):
    if number == largest:
        print(f"{i}...", end=' ')
print()
# lowest number position
print(f"O menor número na lista foi {smaller} nas posições", end=' ')
for i, number in enumerate(listnumbers, start=1):
    if number == smaller:
        print(f"{i}...", end='')
