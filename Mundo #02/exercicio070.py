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
    
    print('Deseja cadastrar um produto?')
    opcao = int(input('[1- Sim]   |  [2- Não]\n'))
    
    if opcao == 1:
        
        produto = str(input('Nome do produto: '))
        preco = float(input('Preço: '))
        
        total += preco
        
        # iniciar as variaveis
        if cont == 0:
            menorPreco = preco
            prodMaisBarato = produto
        
        if preco < menorPreco:
            prodMaisBarato = produto
            
        # contador para produtos maiores que mil reais
        if preco > 1000:
            custoMaiorDeMil += 1
    
    elif opcao == 2:
        print('Encerrando programa...')
        break
    else:
        print('[ERRO]')

print(f'O valor total: R${total:.2f}')
print(f'{custoMaiorDeMil} produtos custando mais de R$1.000,00')
print(f" O produto mais barato da compra foi :{prodMaisBarato}!")
