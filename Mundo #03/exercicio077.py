# Exercício Python 077: Crie um programa que tenha uma tupla
# com várias palavras (não usar acentos). Depois disso, você
# deve mostrar, para cada palavra, quais são as suas vogais.

palavras = ('Cafe', 'Dormir', 'Cachorro', 'Arvore',
            'Montanha', 'Dinheiro', 'Presidente', 'Genocida')

for palavra in palavras:
    print(f'\nNa palavra {palavra} temos - ', end=' ')
    for letra in palavra:
        if letra.lower() in 'aeio':
            print(letra.upper(), end=' ')
