# Exercício Python 70: Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
#
# A) qual é o total gasto na compra.
#
# B) quantos produtos custam mais de R$1000.
#
# C) qual é o nome do produto mais barato.

print('''------------------------
╔═╗┌─┐┌┬┐┌─┐┬  ┌─┐┌─┐┌─┐
║  ├─┤ │ ├─┤│  │ ││ ┬│ │
╚═╝┴ ┴ ┴ ┴ ┴┴─┘└─┘└─┘└─┘
------------------------''')

total = custoMaiorDeMil = cont = menorPreco = 0
prodMaisBarato = ''

while True:
    
    produto = str(input('Nome do produto: '))
    preco = float(input('Preço: '))
    
    cont += 1
    total += preco
    
    # iniciar as variaveis
    if cont == 1 or preco < menorPreco:
        menorPreco = preco
        prodMaisBarato = produto
    if preco > 1000:
        custoMaiorDeMil += 1
    
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Deseja realizar um novo cadastro? (S/N)')).upper().strip()[0]
    if resposta == 'N':
        break

print('--------------------------------')
print(f'Valor total: R${total:.2f}')
print(f'Total de [{custoMaiorDeMil}] produto(s) custando acima de R$1.000,00')
print(f'O produto mais barato da compra foi :{prodMaisBarato}!')
print('--------------------------------')

