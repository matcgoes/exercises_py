# O departamento da qualidade de uma construtora realizou testes em 8
# corpos de prova. Esses dados são armazenados pelo numero sequencial do corpo de prova,
# valor de custo, número de série, resistência teórica de ruptura e o tempo em segundos no teste para ruptura
# Crie uma matriz que armazene todos esses dados sendo que cada coluna represente um tipo de dado. Pede-se:
# a. Mostre todos os dados inseridos.
# b. Deseja-se confirmar quanto tempo o corpo de prova cuja série é 3445 (corpo de prova 4) se rompeu. Mostre esse tempo.
# c. O corpo de prova da posicao 3 apresentou resistencia 15% menor do que a teórica. Atualize esse dado e mostre.
# d. Relatou-se que o mesmo corpo de prova do item b. não apresentou resistencia minima e deve ser descartado. Retire-o da lista.
# e. Mostre os 7 corpos de provas restantes.

corpos_prova = []
for seq in range(1,9):
    print("\nCorpo de prova"+str(seq))
    if seq==4:
        dados=[seq,float(input("Valor de Custo R$: ")),3445,float(input("Resistencia Ruptura: ")),int(input("Tempo até romper: "))]
        corpos_prova.append(dados)
    else:
        dados=[seq,
            float(input("Valor de Custo R$: ")),
           int(input("Número série: ")),
           float(input("Resistencia Ruptura: ")),
           int(input("Tempo até romper: "))]
        corpos_prova.append(dados)
print("\n======== ITEM A =========")
for elemento in corpos_prova:
    print("\nCorpo de prova: \t",elemento[0])
    print("Custo produção (R$):\t",elemento[1])
    print("Número série:\t",elemento[2])
    print("Resistência teórica (kPA):\t",elemento[3])
    print("Tempo até ruptura (s):\t",elemento[4])

print("\n======== ITEM B =========")
for elemento in corpos_prova:
    if elemento[2]==3445:
        print("\nCorpo de prova:\t",elemento[0])
        print("Tempo até ruptura:\t","\t",elemento[4])
        break

print("\n======== ITEM C =========")
for elemento in corpos_prova:
    if elemento[0]==3:
        print("\nResistencia anterior:\t",elemento[3])
        elemento[3]=elemento[3]*0.85
        print("Resistencia atualizada:\t", elemento[3])
        break

print("\n======== ITEM D =========")
for elemento in corpos_prova:
    if elemento[2]==3445:
        print("Removing ......")
        corpos_prova.remove(elemento)

print("\n======== ITEM E =========")
for elemento in corpos_prova:
    print("\nCorpo de prova:\t",elemento[0])
    print("Custo produção (R$):\t",elemento[1])
    print("Número série:\t",elemento[2])
    print("Resistência teórica (kPA):\t",elemento[3])
    print("Temo até ruptura (s):\t",elemento[4])
















