# Faça um programa que use a função valorPagamento para determinar o valor a ser pago por uma prestação de uma conta.
# O programa deverá solicitar ao usuário o valor da prestação e o número de dias em atraso e passar estes valores para a função valorPagamento,
# que calculará o valor a ser pago e devolverá este valor ao programa que a chamou. O programa deverá então exibir o valor a ser pago na tela.
# Após a execução o programa deverá voltar a pedir outro valor de prestação e assim continuar até que seja informado um valor igual a zero para a prestação.
# Neste momento o programa deverá ser encerrado, exibindo o relatório do dia, que conterá a quantidade e o valor total de prestações pagas no dia.
# O cálculo do valor a ser pago é feito da seguinte forma. Para pagamentos sem atraso, cobrar o valor da prestação.
# Quando houver atraso, cobrar 3% de multa, mais 0,1% de juros por dia de atraso.

def valorPagamento(vlr_p,dias_atr):
    if dias_atr > 0:
        return (vlr_p*1.03+0.001*vlr_p*dias_atr)
    else:
        return vlr_p

valor = float(input("Valor da prestacao: "))
dias = int(input("Dias em atraso: "))
lista = []

while valor > 0:
    valor_ajust = valorPagamento(valor,dias)
    lista.append(valor_ajust)
    print("Valor a ser pago: R$",round(valor_ajust,2))
    valor=float(input("Valor da prestacao: "))
    dias=int(input("Dias em atraso: "))

print("\n=====RESUMO DAS PRESTACOES======")
print("\nQuantidade total de prestações:",len(lista))
for index in range(0,len(lista)):
    print("\tPrestacao",index+1,".......R$",round(lista[index],2))