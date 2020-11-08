# Data com mês por extenso. Construa uma função que receba uma data no formato DD/MM/AAAA
# e devolva uma string no formato D de mesPorExtenso de AAAA.
# Opcionalmente, valide a data e retorne NULL caso a data seja inválida.

def dataExtenso(data):
    meses = ["Janeiro","Fevereiro","Março","Abril","Maio","Junho","Julho","Agosto","Setembro","Outubro","Novembro","Dezembro"]
    quebra_data = data.split("/")
    if int(quebra_data[0])>0 and int(quebra_data[0])<32 and int(quebra_data[1])>0 and int(quebra_data[1])<13:
        mes = meses[int(quebra_data[1])-1]
        return (quebra_data[0]+" de "+mes+" de "+quebra_data[2])
    else:
        return "NULL"

data = input("Data a converter (DD/MM/AAAA): ")
convertida = dataExtenso(data)
print(convertida)


