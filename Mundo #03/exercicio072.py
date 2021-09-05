# Exercício Python 72: Crie um programa que tenha uma tupla totalmente
# preenchida com uma contagem por extenso, de zero até vinte.
# Seu programa deverá ler um número pelo teclado (entre 0 e 20)
# e mostrá-lo por extenso
#

tupla = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco',
         'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
         'doze', 'treze', 'quatorze', 'quinze', 'dezesseis',
         'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    while True:
        print('---' * 4)
        num = int(input('Digite um numero entre ZERO E VINTE \n'))
        
        if num < 0 or num > 20:
            print('Número inválido!')
        else:
            print(f'Número {tupla[num]}\n')
        break
    rSair = ' '
    if rSair not in 'SN':
        rSair = str(input('Deseja digitar novamente? S/N')).strip().upper()
    if rSair == 'N':
        print('[....Finalizando....]')
        break
