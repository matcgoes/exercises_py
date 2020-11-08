# Embaralha palavra. Construa uma função que receba uma string como parâmetro e devolva outra string com os carateres embaralhados.
# Por exemplo: se função receber a palavra python, pode retornar npthyo, ophtyn ou qualquer outra combinação possível,
# de forma aleatória. Padronize em sua função que todos os caracteres serão devolvidos em caixa alta ou caixa baixa,
# independentemente de como foram digitados.

import random

def embaralhar(palavra):
    lista=list(palavra)
    randomNumbers = []
    result=[]
    for i in range(len(lista)):
        num = random.randint(0,len(palavra)-1)
        while randomNumbers.count(num) == 1:
            num = random.randint(0, len(palavra) - 1)
        randomNumbers.append(num)
    for j in range(len(randomNumbers)):
        result.append(lista[randomNumbers[j]].upper())
    return "".join(result)

#Jeito mais fácil com shuffle
def embaralhaShuffle(palavra):
    lista=list(palavra)
    random.shuffle(lista)
    return "".join(lista).upper()


word = input("Palavra para embaralhar:  ")
saida1=embaralhar(word)
saida2=embaralhaShuffle(word)
print("----- Os Resultados de ambas funções podem ser diferentes por se tratar de aleatoriedade! -------")
print("\tResultado com Função Loop: ",saida1)
print("\tResultado com Shuffle: ",saida2)









