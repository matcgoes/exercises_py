nome=input("Digite o nome: ")
idade=int(input("Digite a idade: "))
if idade>=65:
    prioridade="SIM"
    print("O paciente " + nome + " possui atendimento prioritário? " + prioridade)
else:
    prioridade="NAO"
    print("O paciente "+nome+" possui atendimento prioritário? "+ prioridade)
