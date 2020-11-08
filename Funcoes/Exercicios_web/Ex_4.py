# Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos.

def soma(a,b,c):
    return a+b+c

arg1 = float(input("Argumento 1: "))
arg2 = float(input("Argumento 2: "))
arg3 = float(input("Argumento 3: "))
resultado = soma(arg1,arg2,arg3)
print(resultado)

# Faça um programa, com uma função que necessite de um argumento.
# A função retorna o valor de caractere ‘P’, se seu argumento for positivo, e ‘N’, se seu argumento for zero ou negativo.

def retornasinal(arg):
    if arg>0:
        return "P"
    else:
        return "N"

valor = float(input("Valor: "))
resultado = retornasinal(valor)
print(resultado)

# Faça um programa com uma função chamada somaImposto. A função possui dois parâmetros formais:
# taxaImposto, que é a quantia de imposto sobre vendas expressa em porcentagem e custo,
# que é o custo de um item antes do imposto. A função “altera” o valor de custo para incluir o imposto sobre vendas.

def somaImposto(taxa,custo):
    return custo*(1+taxa/100)

vlr_taxa=float(input("Qual a taxa em %? "))
vlr_custo=float(input("Qual o custo em R$? "))
vlr_ajustado = somaImposto(vlr_taxa,vlr_custo)
print(vlr_ajustado)
