# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

import time
print('~~*~~' * 10)
print('              Emprestimos Pseudo     '.upper())
print('~~*~~' * 10)


nome = str(input('Nome Completo do Cliente: '))
salario = float(input('Digite seu salário: '))
valorImovel = float(input('Digite o valor do imóvel desejado: '))
anos_pagamento = int(input('Quantos anos o financiamento ? '))

print('...Analizando...')
time.sleep(1.4)

porcent = salario * 30/100

parcela = valorImovel / (anos_pagamento * 12)


if  porcent > parcela :
    print('Sr(a), {}\nEmprestimo aprovado! '.format(nome))
    print('Emprestimo de R${:.2f}\nParcelas de R${:.2f} em {} anos.'.format(valorImovel, parcela, anos_pagamento))
else:
    print('Sr(a), {}'.format(nome))
    print('Emprestimo reprovado! Parcela excede 30% do seu sálario')
