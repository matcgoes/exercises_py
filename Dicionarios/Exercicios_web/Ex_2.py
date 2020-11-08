# Escreva um programa chamado alice_words.py que cria um arquivo de texto chamado alice_words.txt contendo uma lista alfabética de
# todas as palavras, e o número de vezes que cada palavra ocorre, na versão de texto do Alice’s Adventures in Wonderland. 
# (Você pode obter uma versão em texto puro gratuita do livro, junto com muitos outros, a partir de http://www.gutenberg.org.) 
# As primeiras 10 linhas do seu arquivo de saída devem se parecer com:
# 
# Palava	Contador
# a	631
# a-piece	1
# abide	1
# able	1
# about	94
# above	3
# absence	1
# absurd	2
# Quantas vezes a palavra alice aparece no livro? Se você está usando o activecode, simplesmente imprima os resultados
# ao invés de escrever em um arquivo.

import string

def keywithmaxval(d):
    """ a) create a list of the dict's keys and values;
        b) return the key with the max value"""
    v = list(d.values())
    k = list(d.keys())
    return k[v.index(max(v))]

cntword = {}
lenword = {}

f = open("alice_in_wonderland.txt","r",encoding='utf8')
words = f.read().lower()
clean = words.translate(str.maketrans('', '', string.punctuation))
for i in set(clean.split()):
    cntword[i]=clean.count(i)
    lenword[i] = len(i)
f.close()

print("Numero de vezes que 'alice' apareceu: ",cntword.get("alice"))

print(max(lenword.values()))
print(keywithmaxval(lenword))

