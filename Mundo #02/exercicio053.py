# Crie um programa que leia uma frase qualquer e diga se ela
# é um palíndromo, desconsiderando os espaços.
# frases invertidas que mantem o mesmo sentido
# Exemplos de palindromo
# apos a sopa, a sacada da casa, a torre da derrota


# recebendo a string do usuario, colocando em caixa alta
# e tirando os espaços iniciais e finais
frase = str(input('Entre com uma frase: ')).upper().strip()

# dividindo a frase em palavras em uma lista
palavras = frase.split()

# juntando as palavras separadas em uma só
junto = ''.join(palavras)

# string para inverter frase
inverso = junto[::-1]

'''
# outra maneira de se fazer usando o FOR
# variavel para receber a string invertida
inverso = ''

for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
'''

if junto == inverso:
    print('A frase digitada é palindromo')
else:
    print('A frase não é palindromo')
