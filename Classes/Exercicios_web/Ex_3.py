#Source on: https://wiki.python.org.br/ExerciciosClasses
#You can check (some of) solutions here: https://github.com/eliassv/Exercicios-Python/tree/master/classes

# Ex1
# Classe Bola: Crie uma classe que modele uma bola:
#           Atributos: Cor, circunferência, material
#           Métodos: trocaCor e mostraCor

class Bola:
    def __init__(self, cor, circ, material):
        self.cor = cor
        self.circ = circ
        self.material = material
    
    def trocaCor(self):
        self.cor = input("Nova cor: ")
    
    def mostraCor(self):
        print(self.cor)

b1 = Bola("vermelho", 20, "capotao")
# b1.mostraCor()
# b1.trocaCor()
# b1.mostraCor()


# Ex2
# Classe Quadrado: Crie uma classe que modele um quadrado:
    # Atributos: Tamanho do lado
    # Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;

class Quadrado:
    
    def __init__(self,l):
        self.l = l
    
    def mudaLado(self):
        q_mudalado = input("Deseja mudar o lado do quadrado? [s/n] ")
        if q_mudalado.lower() == 's':
            self.l = float(input("Novo lado: "))
        
        
    def retornaLado(self):
        print("O lado do quadrado e: {}".format(self.l))
    
    def calcArea(self):
        return self.l**2
    
q1 = Quadrado(5)
# q1.retornaLado()
# q1.mudaLado()
# q1.retornaLado()
# print("A área do quadrado é: {}".format(q1.calcArea()))


# Ex3
# Classe Retangulo: Crie uma classe que modele um retangulo:
# Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a escolher)
# Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e calcular Perímetro;
# Crie um programa que utilize esta classe. Ele deve pedir ao usuário que informe as medidades de um local.
#  Depois, deve criar um objeto com as medidas e calcular a quantidade de pisos e de rodapés necessárias para o local.

class Retangulo:

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def mudaLado(self):
        escolha = input("Deseja mudar algum lado do retangulo? [s/n]: ").lower()
        if escolha == 's':
            dim = int(input("Qual dimensao?\n1 - base\n2 - altura\n3 - ambas"))
            while dim not in (1,2,3):
                print("Escolha inválida.")
                dim = int(input("Qual dimensao?\n1 - base\n2 - altura\n3 - ambas"))
            if dim == 1:
                self.base = float(input("Nova base: "))
            elif dim == 2:
                self.altura = float(input("Nova altura: "))
            elif dim == 3:
                self.base = float(input("Nova base: "))
                self.altura = float(input("Nova altura: "))
        else:
            print("Dimensoes mantidas.")
    
    def retornaLado(self):
        print(f'A base é : {self.base}')
        print(f'A altura é: {self.altura}')
    
    def calcArea(self):
        return float(self.base)*float(self.altura)
    
    def calcPerim(self):
        return 2*(float(self.base)+ float(self.altura))

def calcMateriais(terr):
    p1 = float(input("Base do piso: "))
    p2 = float(input("Altura do piso: "))
    ap = p1*p2
    qtd = round((terr.calcArea()/ap))
    print('Area do piso: {}'.format(ap))
    print('Voce precisará de {} pisos de {} x {}'.format(qtd,p1,p2))
    print('Voce precisará de {} unidades de comprimento de rodapé'.format(terr.calcPerim()))


# terreno = Retangulo(float(input("Base: ")),float(input("Altura: ")))
# terreno.retornaLado()
# terreno.mudaLado()
# terreno.retornaLado()

# calcMateriais(terreno)


# Ex4
# Classe Pessoa: Crie uma classe que modele uma pessoa:
# Atributos: nome, idade, peso e altura
# Métodos: Envelhercer, engordar, emagrecer, crescer. 
# Obs: Por padrão, a cada ano que nossa pessoa envelhece, sendo a idade dela menor que 21 anos, ela deve crescer 0,5 cm.

class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self,qtd_anos):
        if self.idade <= 21:
            if self.idade + qtd_anos <= 21: 
                self.crescer(qtd_anos)  
            else:
                self.crescer(21-self.idade)                         
        self.idade = self.idade + qtd_anos          
    
    def engordar(self,qtd_peso):
        self.peso = self.peso + qtd_peso
    
    def emagrecer(self,qtd_peso):
        self.peso = self.peso - qtd_peso
    
    def crescer(self, n):
        self.altura = self.altura+n*0.5
    
# p1 = Pessoa('Matheus', 19, 70, 175)
# print(f'O nome da pessoa p1 é: {p1.nome}')
# print(f'A idade da pessoa p1 é: {p1.idade} anos')
# print(f'O peso da pessoa p1 é: {p1.peso} kg')
# print(f'A altura da pessoa p1 é: {p1.altura} cm')
# p1.engordar(5)
# print(f'O peso da pessoa p1 é: {p1.peso} kg')
# p1.emagrecer(8)
# print(f'O peso da pessoa p1 é: {p1.peso} kg')
# p1.envelhecer(4)
# print(f'A idade da pessoa p1 é: {p1.idade} anos')
# print(f'A altura da pessoa p1 é: {p1.altura} cm')


# Ex5
# Classe Conta Corrente: Crie uma classe para implementar uma conta corrente. A classe deve possuir os seguintes atributos:
#  número da conta, nome do correntista e saldo. Os métodos são os seguintes: alterarNome, depósito e saque; 
#  No construtor, saldo é opcional, com valor default zero e os demais atributos são obrigatórios.

from time import sleep
import random

class ContaCorr:

    def __init__(self, numconta, nome, saldo=0.0):
        self.numconta = numconta
        self.nome = nome
        self.saldo = saldo


    def alterarNome(self):
        sleep(2)
        if input("Deseja alterar nome correntista? [s/n]").lower() == 's':
            self.nome = input("Novo nome: ")
        
    def deposito(self):
        sleep(2)
        while True:
            try:
                vlr = float(input("Valor a ser depositado: "))
            except (ValueError, Exception):            
                print('Digite um valor válido.') 
            else:           
                self.saldo += vlr
                print(f'Deposito de R$ {vlr} realizado com sucesso.')
            break
    
    def saque(self):
        sleep(2)
        while True:
            try:
                vlr = float(input("Valor a sacar: "))
                if vlr > self.saldo:                    
                    raise Exception
            except ValueError:
                print('Digite um valor válido.')
            except Exception:
                print('Não há saldo disponível para o valor solicitado.')
            else:
                self.saldo -= vlr
                print(f'Saque de R$ {vlr} realizado com sucesso.')
                break

    def consultaConta(self):
        sleep(2)
        print("Numero da conta: {}".format(self.numconta))
        print("Correntista: {}".format(self.nome))
        print("Saldo em conta: R$ {}".format(round(self.saldo,2)))

    def menu(self):
        sleep(2)
        opcoes = ['Alterar nome correntista','Realizar depósito','Realizar saque','Consultar dados da conta','Sair']
        print(50*'-')
        print('BEM-VINDO AO BANCO X!'.center(50," "))
        print(50*'-')
        for i in range(len(opcoes)):
            print(i+1,' - ',opcoes[i])
        while True:
            try:
                opc = int(input('Opção desejada: '))
                if opc not in [i+1 for i in range(len(opcoes))]:
                    raise Exception
            except Exception:
                print('Digite uma opção válida.')
            else:
                return opc

def menuAcesso():
    print(50*'-')
    print('Menu Principal'.center(50))
    print(50*'-')
    print('1 - Criar conta\n2 - Acessar Conta\n3 - Sair')
    opc_acesso = int(input('Digite uma opção: '))
    while opc_acesso not in (1,2,3):
        print('Opção inválida.')
        opc_acesso = int(input('Digite uma opção: '))
    return opc_acesso

def criarConta(contas):
    nome = input('Digite seu nome: ')
    nm_conta = str(str(random.randrange(1000,9999))+'-'+str(random.randrange(0,9)))
    sleep(3)
    print(f'Conta {nm_conta} criada!')
    contas.append([nm_conta,nome])
    

def acessarConta(contas):
    while True:
        try:
            conta_input = input("Numero da conta para acesso [XXXX-X]: ")
            if conta_input[:4].isdigit() == False or conta_input[4:5] != '-' or conta_input[-1].isdigit() == False:
                raise ValueError
            elif conta_input not in [contas[i][0] for i in range(len(contas))]:
                raise Exception
        except ValueError:
            print('Conta não está no formato especificado')
        except Exception:
            print('Essa conta não se encontra no nosso banco de dados.')  
        else:                       
            for j in range(len(contas)):
                if contas[j][0] == conta_input:
                    a = ContaCorr(contas[j][0],contas[j][1])
                    return a
        
lista_contas = []

def main():    
    e1 = menuAcesso()
    while e1 != 3:
        if e1 == 1:
            criarConta(lista_contas)
        elif e1 == 2:            
            conta = acessarConta(lista_contas)
            opc_conta = conta.menu()
            while opc_conta != 5:
                if opc_conta == 1:
                    conta.alterarNome()
                    opc_conta = conta.menu()
                elif opc_conta == 2:
                    conta.deposito()
                    opc_conta = conta.menu()
                elif opc_conta == 3:
                    conta.saque()
                    opc_conta = conta.menu()
                elif opc_conta == 4:
                    conta.consultaConta()
                    opc_conta = conta.menu()
            print('Saindo do menu da conta...')
            sleep(2)
        e1 = menuAcesso()
    print('Obrigado por utilizar o Banco X!')

# main()

# print(lista_contas)


# Ex6
# Classe TV: Faça um programa que simule um televisor criando-o como um objeto. 
# O usuário deve ser capaz de informar o número do canal e aumentar ou diminuir o volume. 
# Certifique-se de que o número do canal e o nível do volume permanecem dentro de faixas válidas.

from time import sleep

class Tv:

    def __init__(self, canal=1, volume=10):
        self.canal = canal
        self.volume = volume

    def mudarCanal(self):
        canais = [i for i in range(1,11)]
        try:
            cnl_escolha = int(input('Canal: '))
            if cnl_escolha not in canais:
                raise ValueError
        except (ValueError, TypeError):
            sleep(2)
            print('[ERRO] Canal inválido')
        else:
            print(f'Buscando canal {cnl_escolha}...')
            sleep(2)
            self.canal = cnl_escolha
    
    def alterarVolume(self):
        volmax = 100
        volmin = 0
        try:
            vol = int(input('Volume: '))
            if vol > volmax or vol < volmin:
                raise ValueError
        except TypeError:
            sleep(2)
            print('[ERRO] O volume deve ser um valor numérico.')
        except ValueError:
            sleep(2)
            print('O volume deve estar entre 0 e 100.')
        else:
            sleep(2)
            print(vol*'|'+ f' {vol}')
            self.volume = vol

    def interace(self):
        sleep(1)
        print(50*'-')
        print(f'Assistindo canal: {self.canal}')
        print(50*'-')
        print(f'Volume: {self.volume}')
        print(50*'-')


def main():
    tv1 = Tv()
    while True:
        print(100*'=')
        print('1 - Mudar Canal')
        print('2 - Alterar Volume')
        print('3 - Desligar TV')
        print(100*'=')
        opcao = int(input('Selecione opção: '))
        if opcao in (1,2,3):
            if opcao == 1:
                tv1.mudarCanal()
                tv1.interace()
            elif opcao == 2:
                tv1.alterarVolume()
                tv1.interace()
            elif opcao == 3:
                print('Desligando TV...')
                sleep(3)
                break
        else:
            print('Selecione uma opção válida.')
            sleep(1)

# main()


# Ex13/Ex14
# Classe Funcionário: Implemente a classe Funcionário. Um empregado tem um nome (um string) e um salário(um double).
#  Escreva um construtor com dois parâmetros (nome e salário) e métodos para devolver nome e salário. 
#  Escreva um pequeno programa que teste sua classe.
#  Aprimore a classe do exercício anterior para adicionar o método aumentarSalario (porcentualDeAumento) 
#  que aumente o salário do funcionário em uma certa porcentagem
from time import sleep

class Func:

    def __init__(self, nome, salario=500):
        self.nome = nome
        self.salario = salario
    
    def mostraNome(self):
        sleep(1)
        print(f'O nome do funcionário é {self.nome}')
    
    def mostraSalario(self):
        sleep(1)
        print(f'O salário do(a) {self.nome} é {self.salario}')
    
    def aumentaSalario(self,porc):
        sleep(1)
        print(f'Aumentando salário em {porc} %')
        self.salario = self.salario*(1+porc/100)
    
def main():
    f1 = Func('Harry',1000)
    f1.mostraNome()
    f1.mostraSalario()
    f1.aumentaSalario(10)
    f1.mostraSalario()

main()