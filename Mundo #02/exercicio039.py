# Faça um programa que leia o ano de nascimento de um jovem e informe,
# de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar,
# se é a hora exata de se alistar ou se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date
anoAtual = date.today().year
anoNasc = int(input('Ano que Nasceu: '))
idade = anoAtual - anoNasc
if idade > 18:
    print('Já passou da hora de se alistar')
    print('Passou {} anos para alistar, informe-se'.format(idade - 18))
elif idade < 18:
    print('Ainda não está na hora de se alistar!')
    print('Falta {} anos para se alisar.'.format(18 - idade))
else:
    print('Está na hora de se alistar no exército')
    