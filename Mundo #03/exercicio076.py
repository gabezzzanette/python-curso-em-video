# Exercício Python 076: Crie um programa que tenha uma
# tupla única com nomes de produtos e seus respectivos preços,
# na sequência. No final, mostre uma listagem de preços,
# organizando os dados em forma tabular.


tabela = ('Sofá', 950.99,
          'Cadeira de Praia', 74.49,
          'Máquina de Lavar Roupa', 1299.00,
          'Tv 50 polegadas', 2799.99,
          'Notebook', 3500.49)

print("-" * 46)
print(f'{"Tabela de Preços":^45}')
print("-" * 46)

for t in range(0, len(tabela)):
    if t % 2 == 0:
        print(f'{tabela[t]:.<33}', end='')
    else:
        print(f'R${tabela[t]:>10.2f}')
