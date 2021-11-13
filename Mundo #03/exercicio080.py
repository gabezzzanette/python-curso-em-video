# Exercício Python 080: Crie um programa onde o usuário 
# possa digitar cinco valores numéricos e cadastre-os em 
# uma lista, já na posição correta de inserção
# (sem usar o sort()). No final, mostre a lista ordenada na tela.


lista = []

for x in range(0, 5):
    numero = int(input('Digite um numero: '))
    if x == 0 or numero > lista[-1]: 
        lista.append(numero)    #adiciona no final da lista
    else:
        posicao = 0
        while posicao < len(lista): #percorrer a lista
            if numero <= lista[posicao]:
                lista.insert(posicao, numero)   # adiciona o numero na posicao[x]
                break
            posicao += 1

print('===='*20)
print(f'Os números digitados em ordem crescente foram: {lista}')



