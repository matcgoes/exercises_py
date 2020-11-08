# Faça um programa que carregue uma lista com os modelos de cinco carros (exemplo de modelos: FUSCA, GOL, VECTRA etc).
# Carregue uma outra lista com o consumo desses carros, isto é,
# quantos quilômetros cada um desses carros faz com um litro de combustível. Calcule e mostre:
# O modelo do carro mais econômico;
# Quantos litros de combustível cada um dos carros cadastrados consome
# para percorrer uma distância de 1000 quilômetros e quanto isto custará,
# considerando um que a gasolina custe R$ 2,25 o litro. Abaixo segue uma tela de exemplo.

carros = []
consumos = []
for i in range(1,6):
    carros.append(input("Veiculo "+str(i)+" "))
    consumos.append(float(input("km/l? ")))

for elemento in consumos:
    if elemento == max(consumos):
        print("O carro mais economico é: ",elemento)
        break

print("======Cálculos para 1000 km rodados======")
for index in range(0,len(carros)):
    print(carros[index],"\t-",round(1000/consumos[index],2),"\t-","\tR$",round(1000/consumos[index]*2.25,2))

print("=======Fim dos cálculos========")