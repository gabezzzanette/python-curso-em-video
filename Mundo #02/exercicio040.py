#  Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando
#  uma mensagem no final, de acordo com a média atingida:
#
# – Média abaixo de 5.0: REPROVADO
#
# – Média entre 5.0 e 6.9: RECUPERAÇÃO
#
# – Média 7.0 ou superior: APROVADO

notaP = float(input('Primeira nota:'))

notaS = float(input('Segunda nota: '))

media = (notaP + notaS)/2
print('-----*'*5)
if media > 7:
    print('Aprovado!')
elif media  > 5 and media < 6.9:
    print('Recuperação ')
else:
    print('Reprovado')

print('Media final: {}'.format(media))
print('-----*'*5)
