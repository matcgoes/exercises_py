# Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c.
# O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:
# Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os demais valores, sendo encerrado;
# Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
# Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
# Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;

a=float(input("Valor de a: "))
while a == 0 :
    print("A equacao é do 1 grau..."+'\n'+"Programa encerrado.")
    a = float(input("Valor de a: "))
b=float(input("Valor de b: "))
c=float(input("Valor de c: "))
delta=(b**2-4*a*c)
if delta < 0 :
    print("O delta é " ,delta, "ou seja, nao possui raizes reais")
elif delta == 0:
    print("Existe apenas uma raiz: "+ str((-b/2*a)))
    # raiz_1=(-b/2*a)
else:
    print("raiz_1 = " + str((-b+(delta**0.5))/2*a))
    print("raiz_2 = " + str((-b-(delta**0.5))/2*a))