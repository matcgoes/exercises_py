# Nome na vertical em escada. Modifique o programa anterior de forma a mostrar o nome em formato de escada.

def nomeEscada(nome):
    for i in range(len(nome)+1):
        print(nome[:i].upper())

def inversoNomeEscada(nome):
    for i in range(len(nome),0,-1):
        print(nome[:i].upper())

nomeEscada('Fulano')
print("\n")
inversoNomeEscada('Fulano')

# Conta espaços e vogais. Dado uma string com uma frase informada pelo usuário (incluindo espaços em branco), conte:
# quantos espaços em branco existem na frase.
# quantas vezes aparecem as vogais a, e, i, o, u.

vowels = {'a':0,'e':0 ,'i':0 ,'o':0 ,'u':0 ,' ':0 }
def countVowelsnBlank(s):
    for key in vowels.keys():
        vowels[key] = s.lower().count(key)
    for k,v in vowels.items():
        print("{}: {}".format(k,v))

countVowelsnBlank('Eu amo o Python')

# Palíndromo. Um palíndromo é uma seqüência de caracteres cuja leitura é idêntica se feita da direita para esquerda 
# ou vice−versa. Por exemplo: OSSO e OVO são palíndromos. Em textos mais complexos os espaços e pontuação são ignorados. 
# A frase SUBI NO ONIBUS é o exemplo de uma frase palíndroma onde os espaços foram ignorados. 
# Faça um programa que leia uma seqüência de caracteres, mostre−a e diga se é um palíndromo ou não.
import string

def palindromo(s):
    """
    Given a string s, returns if this reverse string is the same as the string
    """
    clean_spont = s.translate(str.maketrans('','',string.punctuation)) #Retira ponutações e adiociona '' no lugar.
    clean_s = clean_spont.strip().replace(' ','').lower() #Tira espaços vazios nas extremidades e no meio da string
    if clean_s == clean_s[::-1]:
        print("\n \"{}\" é palíndromo".format(s))
    else:
        print("\n \"{}\" não é palíndromo".format(s))

palindromo('Subi no onibus!')

# Jogo de Forca. Desenvolva um jogo da forca. O programa terá uma lista de palavras lidas de um arquivo texto e escolherá 
# uma aleatoriamente. O jogador poderá errar 6 vezes antes de ser enforcado.
# Digite uma letra: A
# -> Você errou pela 1ª vez. Tente de novo!

# Digite uma letra: O
# A palavra é: _ _ _ _ O

# Digite uma letra: E
# A palavra é: _ E _ _ O

# Digite uma letra: S
# -> Você errou pela 2ª vez. Tente de novo!

import random

with open('words_hangman.txt','r') as wdfile:
    word_list = wdfile.read().upper().split()
    word = (word_list[random.randint(0,len(word_list))])#Picking a random word from word list 
    letters = list(word) #turning the word into a letter list 
    empty = ["_" for i in range(len(letters))]

errors = 0
tries = []
while errors < 7 and empty.count("_") !=0:
    lt_input = input("\nEnter a letter: ").upper()
    while lt_input in tries:
        print("\nWarning: you've already tried this letter.")
        lt_input = input("Enter a letter: ").upper()
    tries.append(lt_input)
    v = [i for i in range(len(letters)) if letters[i] == lt_input]
    if len(v)== 0:
        errors += 1
        print("You've missed for the {} time.".format(errors))
    else:
        for k in v:
            empty[k] = lt_input
    print("\n"+' '.join(empty))
if empty.count("_") > 0 :
    print("\nYou LOSE!")
    print("The word was {}".format(word))
else:
    print("\nYou WIN!")