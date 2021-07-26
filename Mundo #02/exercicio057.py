# -------------------------------------------------
# Faça um programa que leia o sexo de uma pessoa,
# mas só aceite os valores ‘M’ ou ‘F’.
# Caso esteja errado, peça a digitação novamente até
# ter um valor correto.
#--------------------------------------------------

print('-------- Cadastro --------')
print('F - feminino')
print('M - masculino')
sexo = input('Digite o sexo: ').strip().upper()[0]

while sexo not in 'FfMm':
    sexo = str(input('Erro! Digite uma opção válida! Sexo : F/ M ?')).strip().upper()[0] # tirando espaços | maiuscula | primeira letra
print('Sexo {} cadastrado ...'.format(sexo))
print('Cadastro concluído com sucesso')
