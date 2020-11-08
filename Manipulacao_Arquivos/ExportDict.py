from Dicionarios_Package.Funcoes import *

usuarios={}
opcao=perguntar()
while opcao=="I" or opcao=="P" or opcao=="E" or opcao=="L":
	if opcao=="I":
		inserir(usuarios)
	if opcao=="P":
		pesquisar(usuarios,input("Quem deseja pesquisar? ").upper())
	if opcao=="E":
		excluir(usuarios, input("Quem deseja excluir? ").upper())
	if opcao=="L":
		listar(usuarios)
	opcao = perguntar()

salvar(usuarios)

