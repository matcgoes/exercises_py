# Desenha moldura. Construa uma função que desenhe um retângulo usando os caracteres ‘+’ , ‘−’ e ‘| ‘.
# Esta função deve receber dois parâmetros, linhas e colunas.

def drawRectangle(rows,columns):
    print("Drawing Rectangle "+str(rows)+"x"+str(columns))
    for i in range(rows):
        for j in range(columns):
            if i==0 or i==rows-1:
                print("-",end="  ")
            elif j==0 or j==columns-1:
                print("|",end="  ")
            else:
                print("+",end="  ")
        print()

drawRectangle(int(input("rows: ")),int(input("columns: ")))