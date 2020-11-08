# Faça um programa que calcule o número médio de alunos por turma.
# Para isto, peça a quantidade de turmas e a quantidade de alunos para cada turma.
# As turmas não podem ter mais de 40 alunos.

# 1o Método: Utilizando While
qtd_turma=int(input("Quantidade de turmas: "))
contador = 1
sum_alunos = 0
while contador <= qtd_turma:
    qtd_alunos=int(input("Quantos alunos na turma "+str(contador)+"? " ))
    while qtd_alunos > 40:
        print("Quantidade de alunos deve ser no máximo 40!!!")
        qtd_alunos = int(input("Quantos alunos na turma " + str(contador) + "? "))
    contador = contador + 1
    sum_alunos = sum_alunos + qtd_alunos
print("A média de alunos por turma é de: ", sum_alunos/qtd_turma, "!")

# 2o Método: Utilizando For
qtd_turma=int(input("Quantidade de turmas: "))
sum_alunos = 0
for i in range(1,qtd_turma+1):
    qtd_alunos=int(input("Quantos alunos na turma "+str(i)+"? "))
    while qtd_alunos > 40 :
        print("Quantidade de alunos deve ser no máximo 40!!")
        qtd_alunos=int(input("Quantos alunos na turma "+str(i)+"? "))
    sum_alunos = sum_alunos + qtd_alunos
print("A média de alunos por turma é de: ", sum_alunos/qtd_turma, "!")




