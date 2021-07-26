#
#Exercício Python 62: Melhore o DESAFIO 61
# perguntando para o usuário se ele quer
# mostrar mais alguns termos. O programa
# encerrará quando ele disser que quer mostrar
# 0 termos.

print('-------- Progressão Aritmética --------')
p_termo = int(input('Primeiro termo: '))
razao = int(input('Razão : '))
cont = -1
qtdTermos = 10

while cont != 0:
    cont2 = 1
    
    if cont == -1:
        cont = 1
        while cont <= 10:
            print('{} '.format(p_termo))
            p_termo += razao
            cont += 1
    
    else:
        while cont2 <= cont:
            print('{} '.format(p_termo))
            p_termo += razao
            cont2 += 1
        
    cont = int(input('Deseja mais quantas PA? '))
    qtdTermos += cont
print('[ fim da progressão aritmética ]')
print('Foram mostrados {} termos '.format(qtdTermos))
