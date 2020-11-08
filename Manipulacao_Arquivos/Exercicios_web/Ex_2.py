# A ACME Inc., uma empresa de 500 funcionários, está tendo problemas de espaço em disco no seu servidor de arquivos. 
# Para tentar resolver este problema, o Administrador de Rede precisa saber qual o espaço ocupado pelos usuários, 
# e identificar os usuários com maior espaço ocupado. Através de um programa, baixado da Internet, 
# ele conseguiu gerar o seguinte arquivo, chamado "usuarios.txt".

# /1048576

from tabulate import tabulate

def convertToMb(valbyte):
    return round(valbyte/1048576,2)

def percentageUsage(valbyte,totalspace):
    return str(round(100*valbyte/totalspace,2))+"%"

f = open("usuarios.txt","r")
totallist = []
datalist = f.read().split()
sizelist = list(map(int,datalist[1::2]))
namelist = datalist[0::2]
for i in range(len(sizelist)):
    totallist.append([namelist[i],convertToMb(sizelist[i]),percentageUsage(sizelist[i],sum(sizelist))])
f.close()

headline = "ACME Inc."+15*" "+"Uso do espaço em disco pelos usuários\n"+80*"-"+"\n"

with open("report.txt","w") as report:
    report.write(headline+"\n")   
    report.write(tabulate(totallist, headers=['User', 'Size', '% Usage'],tablefmt='orgtbl')+"\n")
    report.write("\nDisk Usage Space: "+str(round(convertToMb(sum(sizelist)),2))+" MB")
    report.write("\nAverage Disk Usage: "+str(round(convertToMb(sum(sizelist)/len(sizelist)),2))+" MB")


