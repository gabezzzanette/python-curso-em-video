# -------------------------------------------------------------------
# Exercício Python 56: Desenvolva um programa que leia o nome,
# idade e sexo de 4 pessoas. No final do programa,
# mostre: a média de idade do grupo, qual é o nome
# do homem mais velho e quantas mulheres têm menos de 20 anos.
# -------------------------------------------------------------------

# váriaveis
soma_idades = 0
n_homem_mais_velho = ''
maior = 0
contador = 0

# Cadastro
print('===== Cadastro =====')
for x in range(1, 5):
    
    print('n : {}'.format(x))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo[F/M]: ')).strip()
    
    # soma das idade
    soma_idades += idade
    
    # maior idade entre os homens
    if sexo in "Mm" and idade > maior:
        maior = idade
        n_homem_mais_velho = nome
    
    # contagem de mulheres que são < 20
    if sexo in "Ff" and idade < 20:
        contador += 1


# Função para determinar a frase final
def verbo(cont):
    if cont == 1:
        palavra = 'existe uma mulher'
    else:
        palavra = str('existem {} mulheres'.format(cont))
    return palavra


# media das idades
media = soma_idades / 4

# imprimindo resultados
print('====' * 7)
print('A media de idades foi : {}'.format(media))
print('O Sr. {} é o mais velho entre os homens com {} anos'.format(n_homem_mais_velho, maior))
print('e {} com menos de 20 anos'.format(verbo(contador)))
print('====' * 7)
