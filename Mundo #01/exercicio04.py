# Fazer um programa que leia algo do teclado e imprima na tela algumas coisas sobre os dados

dado_usuario = input('Digite algo: ')

print('O dado digitado pelo usuario foi {}'.format(dado_usuario))
# Dados inseridos via input sempre serao lidos como strings
print('O tipo do dado digitado é: ', type(dado_usuario),' por ser lido com comando input')
print('O dado é um alfanumerico ? ', dado_usuario.isalnum())
print('O dado é um numero? ', dado_usuario.isnumeric())
print('O dado é um caractere ? ', dado_usuario.isalpha())
print('O dado é contem somente espaços em branco? ', dado_usuario.isspace())
print('O dado é um numero decimal ? ', dado_usuario.isdecimal())
print('O dado é identificador ? ' , dado_usuario.isidentifier())
print('O dado esta na tabela ASCII? ', dado_usuario.isascii())
print('O dado esta em minusculo? ', dado_usuario.islower())
print('O dado esta em MAIUSCULO? ', dado_usuario.isupper())
print('O dado é um digito? ', dado_usuario.isdigit())
print('O dado é um printtable? ', dado_usuario.isprintable())
print('O dado é um titulo? ', dado_usuario.istitle())

