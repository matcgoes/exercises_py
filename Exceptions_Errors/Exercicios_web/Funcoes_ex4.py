
from tabulate import tabulate
from time import sleep

def listaOpcoes(msg):
    """
    Função que lista as opções do sistema a serem escolhidas pelo usuário.
    """
    while True:
        print(50*"-"+"\n"+20*"\t"+"MENU PRINCIPAL\n"+50*"-")
        print("1 - Ver pessoas cadastradas")
        print("2 - Cadastrar nova pessoa")
        print("3 - Sair do sistema")
        try:
            opt = int(input(msg))
            if opt not in (1,2,3):
                raise Exception
        except Exception:
            print("Por favor, escolha uma opção válida.")
        else:
            return opt

# listaOpcoes(50*"-"+"\nSua Opção: ")

def listaCadastro(arquivo):
    """
    Função que lê um arquivo especificado pelo usuário, e mostra em formato de tabela.
    """    
    try:    
        file = open(arquivo,'r')
    except FileNotFoundError:
        print(f'ERRO: O arquivo \"{arquivo}\" nao existe.')
    else:
        lst = [s.split(",") for s in file.readlines()]
        print(tabulate(lst,headers=['Nome','Idade']))
        file.close()

def novoCadastro(arquivo):
    while True:
        try:
            nome = input("Nome: ")           
            if nome == "" or nome.count(" ") == len(nome) or nome.isdigit():
                raise Exception
        except Exception:
            print("ERRO: Esse tipo de dado não é válido.")
        else:
            while True:
                try:
                    idade = int(input("Idade: "))
                except (ValueError, TypeError):
                    print("ERRO: Esse tipo de dado não é válido.")
                else:                                   
                    with open(arquivo,'a') as file:
                        file.write(f"{nome}, {idade} anos\n")
                        print("Cadastro realizado com sucesso.")
                        break
            break
                    
def sair():
    print("Saindo do sistema...")
