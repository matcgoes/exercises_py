# These exercises were taken from https://github.com/chrhobbs/exercise-python-json-parsing

#Foi possível criar uma solução utilizando dicionários e outra utilizando listas.

import json
from tabulate import tabulate


with open("ttjson.json","r") as jsonfile:
    data = json.load(jsonfile)["imdata"]
    
header = str("Interface Status"+
        "\n================================================================================")

#Solução com listas       
# lst = []
# with open("ex_1.txt","w") as answerfile:    
#     answerfile.write(header+"\n")
#     for key in data:
#         dn = key.get("l1PhysIf").get("attributes").get("dn")
#         descr = key.get("l1PhysIf").get("attributes").get("descr")
#         speed = key.get("l1PhysIf").get("attributes").get("speed")
#         mtu = key.get("l1PhysIf").get("attributes").get("mtu")
#         lst.append([dn,descr,speed,mtu])
#     answerfile.write(tabulate(lst,headers=["DN","Description", "Speed", "MTU"],tablefmt='github'))


#Solução com dicionários
dictionary = {}
dictionary["dn"] = [key.get("l1PhysIf").get("attributes").get("dn") for key in data]
dictionary["descr"] = [key.get("l1PhysIf").get("attributes").get("descr") for key in data]
dictionary["speed"] = [key.get("l1PhysIf").get("attributes").get("speed") for key in data]
dictionary["mtu"] = [key.get("l1PhysIf").get("attributes").get("mtu") for key in data]
print(dictionary)

with open("ex331.txt","w") as answerfile:   
    answerfile.write(header+"\n") 
    answerfile.write(tabulate(dictionary,headers=["DN","Description", "Speed", "MTU"],tablefmt='orgtbl'))
    


