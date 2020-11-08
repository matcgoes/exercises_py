# Faça um programa que leia um arquivo texto contendo uma lista de endereços IP e 
# gere um outro arquivo, contendo um relatório dos endereços IP válidos e inválidos.

import random
from tabulate import tabulate

write_ip = ['0.12.15.253','200.135.80.9', '192.168.1.1', '8.35.67.74', '257.32.4.5', '85.345.1.2', '1.2.3.4', '9.8.234.5', '192.168.0.256']
# print(write_ip)

"""
If you want to know how to classify an IP into Valid or Invalid, check it out here: https://tinyurl.com/ydcffz5z
"""

# with open('ips.txt','w') as db:
#     for ip in write_ip:
#         db.write(ip+"\n")

with open ('ips.txt','w') as fip:
    for i in range(100):
        fip.write(str(random.randrange(256))+"."+str(random.randrange(256))+"."+str(random.randrange(256))+"."+str(random.randrange(256))+"\n")


def classifyIp(ip):
    if int(ip.split('.')[0]) in range(1,127):
        return 'A'
    elif int(ip.split('.')[0]) in range(128,192):
        return 'B'
    elif int(ip.split('.')[0]) in range(192,224):
        return 'C'
    else:
        return 'This IP adress cannot be classified.'

def isValid(ip):
    print("Checking Ip: ", ip)
    classe = classifyIp(ip)
    if all(int(ip.split('.')[i]) in range(0,256) for i in range(1,4)):
        if classe == 'A' and (ip.split('.')[1::] != ['255','255','255'] and ip.split('.')[1::] != ['0','0','0']) :
            return True
        elif classe == 'B' and (ip.split('.')[2::] != ['255','255'] and ip.split('.')[2::] != ['0','0']):
            return True
        elif classe == 'C' and (ip.split('.')[3] != '255' and ip.split('.')[3] != '0'):
            return True
        else:
            return False
    else:
        return False

f = open('ips.txt','r')
iplist = f.read().splitlines()
f.close()
        
# with open('classified_ips.txt','w') as w_file:
#     validips=[]
#     invalidips=[]
#     w_file.write("-----Valid IP Adresses-----\n")
#     for ip in iplist:
#         if isValid(ip)==True:
#             w_file.write(ip+"\n")
#     w_file.write("\n")
#     w_file.write("-----Invalid IP Adresses-----\n")
#     for ip in iplist:
#         if isValid(ip)==False:
#             w_file.write(ip+"\n")


validips=[]
invalidips=[]
for ip in iplist:
    if isValid(ip)==True:
        validips.append(ip.split())
    elif isValid(ip)==False:
        invalidips.append(ip.split())

print(validips)
print(invalidips)

headline = "IP Analysis from matcgoes@gcorp.isf"+3*"\n"

with open('classi_ips.txt','w') as w_file:
    w_file.write(headline)
    w_file.write(tabulate(validips, headers=['Valid IPs'],tablefmt='orgtbl')+2*"\n")
    w_file.write(tabulate(invalidips, headers=['Invalid IPs'],tablefmt='orgtbl')+"\n")