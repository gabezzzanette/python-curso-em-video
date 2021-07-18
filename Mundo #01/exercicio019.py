# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que #ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

from random import choice

alunos = ['Ana', 'Bruna','Gabe','Natan']
print('O aluno escolhido pelo professor foi: {}'.format(choice(alunos)))