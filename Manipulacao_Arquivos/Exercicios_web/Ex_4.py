#Fonte: https://panda.ime.usp.br/pensepy/static/pensepy/10-Arquivos/files.html#exercicios
# Aqui está um arquivo notas_estudantes.dat que contém uma linha para cada aluno de uma turma de estudantes. 
# O nome de cada estudante está no início da cada linha e é seguido pelas suas notas.

# Usando o arquivo texto notas_estudantes.dat escreva um programa que imprime o nome dos alunos que têm mais de seis notas.
def notasAlunos(qtdmin):
    nomes = [key[0] for key in dicio_notas.items() if len(key[1]) > qtdmin] #Nomes cujas qtds de notas sao maiores que "n"
    print("Nome que tiveram qtd. de notas maiores que:",qtdmin)
    for i in nomes:
        print(i,end=" ")
    print()

# Usando o arquivo texto notas_estudantes.dat escreva um programa que calcula a média das notas de cada estudante 
# e imprime o nome e a média de cada estudante.
# Usando o arquivo texto notas_estudantes.dat escreva um programa que calcula a nota mínima e máxima de cada estudante e 
# imprima o nome de cada aluno junto com a suam notá máxima e mínima.
def estatNotas(dic):
    print(2*"\n"+"--------Estatísticas da Notas--------")
    for key,value in dic.items():
        print("\nNome.......:",key)
        print("Nota mín.....:",min(list(value)))
        print("Média........:",round(sum(list(value))/len(list(value)),2))
        print("Nota máx.....:",max(list(value)))

dicio_notas = {}
with open('notas_estudantes.dat','r') as f:
    notas = [s.split() for s in f.readlines()]
    for elements in notas:
        dicio_notas[elements[0]] = [int(i) for i in elements[1::]] #Preenchendo dados no dicionário.
    notasAlunos(2)
    estatNotas(dicio_notas)