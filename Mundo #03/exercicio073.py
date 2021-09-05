#
# Exercício Python 73: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do
# Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
#
# a) Os 5 primeiros times.
#
# b) Os últimos 4 colocados.
#
# c) Times em ordem alfabética.
#
# d) Em que posição está o time da Chapecoense.
#

tabelaBrasileirao = ('Atlético Mineiro', 'Palmeiras', 'Fortaleza', 'Bragantino',
                     'Flamengo', 'Athletico-PR', 'Atlético Goianiense', 'Ceará',
                     'Santos', 'Corinthians', 'Internacional', 'Juventude', 'Bahia',
                     'São Paulo', 'Fluminense', 'Cuiabá', 'Sport Recife', 'América-MG',
                     'Grêmio', 'Chapecoense')
count = 0

print(f'''
            +------------------------------------------------------+
            |        TABELA CAMPEONATO BRASILEIRO DE FUTEBOL       |
            +------------------------------------------------------+
    ''')

while True:
    
    rVerTabela = ' '
    if rVerTabela not in 'SN':
        rVerTabela = str(input('Deseja ver a tabela inteira ? S/N'))
    if rVerTabela == 'S':
        print(f'{tabelaBrasileirao}\n')
        break
    if rVerTabela == 'N':
        break

print(f'Primeiros 05 times da Tabela:\n{tabelaBrasileirao[:5]}\n')
print(f'Os últimos 04 colocados:\n{tabelaBrasileirao[-4:]}\n')
print(f'Ordem alfabética da Tabela:\n{sorted(tabelaBrasileirao)}\n')
print(f'O time Chapecoense está na posição {tabelaBrasileirao.index("Chapecoense") + 1}')