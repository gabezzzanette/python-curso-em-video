# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1250,00, calcule um aumento de 10%.
# Para os inferiores ou iguais, o aumento é de 15%.

funcionario = str(input('Nome: '))
salario = float(input('Salário: '))

if salario > 1250.0:
    salarioNovo = salario + (salario * (10/100))
    aumento = 10
else:
    salarioNovo = salario + (salario * (15/100))
    aumento = 15
print('Bom dia, senhor(a) {},'.format(funcionario))
print('Seu salário de R${} teve um aumento de {}% e salario atual é de R${}'.format(salario,aumento, salarioNovo))



