# Reverso do número. Faça uma função que retorne o reverso de um número inteiro informado. Por exemplo: 127 -> 721.

def inverteNum(n):
    inverso = 0
    while n > 0:
        #Ex: resto de 123/10 -> 3. Note que aqui o resto sempre será um numero inteiro entre 1 e 9
        resto = n%10
        #Aqui estamos inserindo o resto na ultima casa. Ex: se o inverso for 2, entao 2*10+resto = 2resto
        inverso = inverso*10+resto
        #Aqui estamos fazendo com que pule para a próxima casa. Se o numero era 123, agora vamos utilizar 12 e iterar de novo
        n = int(n/10)
    return inverso

numero = int(input("Qual numero deseja inverter? "))
resultado = inverteNum(numero)
print("\nO inverso é:",resultado)


