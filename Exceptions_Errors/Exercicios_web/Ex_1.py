# Devido à falta de exercicios nesse assuntona web, os mesmos foram criados por eu mesmo.
# Created by: Matheus Cabreira de Goes

# Q1: Crie um programa que divida dois numeros inteiros. Caso o denominador seja zero, mostre a mensagem
# que é impossível dividir por zero.
a = int(input("Numerador: "))
b = int(input("Denominador: "))
try:
    rz = a/b
except ZeroDivisionError:
    print("Não é possível dividir por 0")
else:
    print("O resultado é {}".format(rz))


# Q2: Com o mesmo enunciado de Q1, crie um programa que nao aceite strings/valores omitidos e que mostre uma mensagem caso
# o usuario interromper a execução
try:
    c = int(input("Numerador: "))
    d = int(input("Denominador: "))
    v = c/d
except ZeroDivisionError as e1:
    print("Não é possível dividir por zero")
except ValueError as e2:
    print("O valor informado deve ser um numero inteiro!")
except KeyboardInterrupt as e3:
    print("O usuário interrompeu o programa.")
else:
    print("Sucesso. O valor de \"v\" é {}".format(v))
finally:
    print("\nExecutando finally...")


#Q3: Crie um programa que tente abrir um arquivo txt e, caso o mesmo nao exista, imprima uma mensagem de erro que
# o mesmo nao existe. Se existir, leia-o e feche-o.
try:
    f = open('checa_existencia.txt','r')
except FileNotFoundError:
    print("O arquivo solicitado não existe.")
else:
    print("Abrindo arquivo...")
    print(f.read())
    f.close()
finally:
    print("Finally...")

# Q4: Crie um programa que abra um arquivo e realize a divisao de dois numeros inteiros ao mesmo tempo. 
# Caso exista erro, aponte-o
try:
    f = open('checa_existencia.txt')
    n1 = int(input("N1: "))
    n2 = int(input("N2: "))
    div = n1/n2
except Exception as err:
    print("Houve um erro:",err)
else:
    print(f.read())
    print("O arquivo \"{}\" existe e o resultado de \"div\" e: {}".format(f.name,div))
    f.close()    
finally:
    print("Executando finally...")


# Q5: Tente abrir um arquivo .txt, no entanto, se o arquivo for o "corrompido.txt", force um erro.
try:
    f = open('corrompido.txt')
    if f.name == 'corrompido.txt':
        raise Exception
except Exception as err:
    print("ERRO!")
else:
    print(f.read())