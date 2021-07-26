#  Elabore um programa que calcule o valor a ser pago por um
#  produto, considerando o seu preço normal e condição de pagamento:
#
# – à vista dinheiro/cheque: 10% de desconto
#
# – à vista no cartão: 5% de desconto
#
# – em até 2x no cartão: preço formal
#
# – 3x ou mais no cartão: 20% de juros

print('$____'*8)
precoNormal = float(input('\nValor do produto: '))

cod = int(input('''Digite o número da operação de pagamento: 
    [1] à vista no dinheiro ou cheque
    [2] à vista no cartão
    [3] 2x no cartão
    [4] 3x ou mais no cartão
'''))

if cod == 1:
    print('à vista dinheiro/cartão : 10% de desconto')
    print('Valor final à pagar R${:.2f}'.format(precoNormal - precoNormal*0.10))
elif cod == 2:
    print('à vista no cartão: 5% de desconto')
    print('Valor final à pagar R${:.2f}'.format(precoNormal - precoNormal * 0.05))
elif cod == 3:
    print('em até 2x no cartão: preço formal')
    print('Valor final à pagar R${:.2f} em 2 x R$ {:.2f}'.format(precoNormal, precoNormal/2))
elif cod == 4:
    print('3x no cartão: 20% de juros')
    print('Valor final à pagar R${:.2f} em 3 x R$ {:.2f} '.format(precoNormal + precoNormal * 0.2, precoNormal / 3))
else:
    print('Codigo da operação não existe!!\n')

print('$____'*8)