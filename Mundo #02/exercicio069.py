#
# Exercício Python 69: Crie um programa que leia a idade
# e o sexo de várias pessoas.
# A cada pessoa cadastrada, o programa deverá perguntar
# se o usuário quer ou não continuar. No final, mostre:
#
# A) quantas pessoas tem mais de 18 anos.
#
# B) quantos homens foram cadastrados.
#
# C) quantas mulheres tem menos de 20 anos.

cMaiorDeDezoitoAnos = 0
cHomensCadastrados = 0
cMulheresComMenosDeVinte = 0
print('----**---------**---------**-----')
while True:
    
    print('Bem-vindo')
    print('[1 - SIM]       |     [2 - NÃO]')
    
    respostaSeUsuarioQuerCadastrar = int(input('Deseja cadastrar ?'))
    #cadastrando um usuario
    if respostaSeUsuarioQuerCadastrar == 1:
        print('---*--- Cadastro ---*---')
        print('Vamos lá! Nos conte sua')
        idade = int(input('Idade: '))
        if idade >= 18:
            cMaiorDeDezoitoAnos += 1
            print(cMaiorDeDezoitoAnos)
            
        print('[1 - MASCULINO]       |     [2 - FEMININO]')
        print('Ok! Agora o seu')
        sexo = int(input('Sexo:'))
        if sexo == 1:
            cHomensCadastrados += 1
            print(cHomensCadastrados)
        elif sexo == 2:
            if idade < 20:
                cMulheresComMenosDeVinte += 1
                print(cMulheresComMenosDeVinte)
        else:
            print('Opção inválida!!')
    #finalizando programa
    elif respostaSeUsuarioQuerCadastrar == 2:
        print('Saindo do programa.\nVolte sempre!')
        break
    else:
        print('Opção inválida!!')
    

print(f'''Foram registradas {cMaiorDeDezoitoAnos} pessoas com mais de 18 anos, no total
foram cadastrados {cHomensCadastrados} homens e {cMulheresComMenosDeVinte} mulheres
com menos de 20 anos.''')
