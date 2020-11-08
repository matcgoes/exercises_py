# Esse exercício é referente ao Exercício 114 mencionado no seguinte vídeo:
# https://www.youtube.com/watch?v=xz2B3bfNjEk

#Crie um codigo em Python que teste se o site Pudim está acessível pelo computador usado.

# from selenium import webdriver
# from time import sleep
import socket
# PATH = 'C:\Program Files (x86)\chromedriver.exe'
# driver = webdriver.Chrome(PATH)
# site = "www.pudim.com.br"

def acessivel(site):
    try:
        socket.gethostbyname(site)
    except Exception:
        return ("O site \""+site+"\" nao esta acessivel no momento...")
    else:
        return ("O site \""+site+"\" foi acessado com sucesso!")

print(acessivel("www.pudim.com.br"))




