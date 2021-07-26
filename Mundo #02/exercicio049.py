# mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

print('='*15)
print('Tabuada')

num = int(input('Escolha qual tabuada quer ver '))

for n in range (1, 11):
    print('{} x {} = {}'.format(n , num ,n * num))
