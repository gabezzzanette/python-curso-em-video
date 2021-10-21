# Exercício Python 079: Crie um programa onde
# o usuário possa digitar vários valores numéricos
# e cadastre-os em uma lista. Caso o número já exista
# lá dentro, ele não será adicionado. No final, serão
# exibidos todos os valores únicos digitados, em ordem crescente.
# reeceber os valores do usuario e guardar em uma lista

numblist = list()

while True:
    
    numero = input("Digite um número:")
    if not numero.isnumeric():
        print("Digite apenas numeros!")
        print(f'{numblist}')
    elif numero not in numblist:
        numblist.append(numero)
    else:
        print("Número duplicado! Não será adicionado na lista.")
    
    respSair = ' '
    while True:
        respSair = str(input("Deseja digitar mais um número? (S/N)"))
        if respSair not in 'SsNn':
            print('Tente novamente')
        else:
            break
    if respSair in 'Nn':
        break
    
# Lista em Ordem Crescente
numblist.sort(key=int)
print(f'Os números digitados na lista foram: {numblist}')




