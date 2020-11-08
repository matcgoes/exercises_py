# Esse exercício é referente ao Exercício 115 [ADAPTADO] mencionado no seguinte vídeo:
# https://www.youtube.com/watch?v=xz2B3bfNjEk

# Crie um pequeno sistema modularizado que permite cadastrar pessoas pelo seu nome e idade em um arquivo JSON
# O sistema terá 3 opções: Cadastrar uma nova pessoa, listar as pessoas cadastradas ou sair.

from Funcoes_ex4 import *


opcao = listaOpcoes(50*"-"+"\nSua Opção: ")
while opcao in (1,2):
    if opcao == 1:
        listaCadastro('cadastros.txt')
        sleep(2)
        opcao = listaOpcoes(50*"-"+"\nSua Opção: ")
    elif opcao == 2:
        novoCadastro('cadastros.txt')
        sleep(2)
        opcao = listaOpcoes(50*"-"+"\nSua Opção: ")    
    elif opcao == 3:
        sleep(2)
        sair()


