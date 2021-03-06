# A Confederação Nacional de Natação precisa de um programa que leia o
# ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
#
# – Até 9 anos: MIRIM
#
# – Até 14 anos: INFANTIL
#
# – Até 19 anos: JÚNIOR
#
# – Até 25 anos: SÊNIOR
#
# – Acima de 25 anos: MASTER

from datetime import date

print('-----*'*10)
print('.               .Conferencia Nacional de Natação.          .')
print('-----*'*10)

print('- Categorias - \n')
print('''  Mirin
  Infantil
  Júnio
  Sênior
  Master\n''')

ano = int(input(' [ Digite o ano do seu nascimento: ]'))

idade = date.today().year - ano

if idade <= 9:
    print('MIRIM')
elif idade <= 14:
    print('INFANTIL')
elif idade <= 19:
    print('JÚNIOR')
elif idade <= 25:
    print('SÊNIOR')
else:
    print('MASTER')
