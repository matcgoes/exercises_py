# Escreva um programa que lê em uma sequência da linha de comando e retorna uma tabela com as letras do alfabeto
# em ordem alfabética que ocorrem na sequência junto com o número de vezes que cada letra ocorre.
# Ignore se as letras são maiúsculas ou minúsculas. Um exemplo de execução do programa ficaria assim:
#
# $ python letter_counts.py "ThiS is String with Upper and lower case Letters."
# a  2
# c  1
# d  1
# e  5
# g  1
# h  2
# i  4
# l  2
# n  2
# o  1
# p  2
# r  4
# s  5
# t  5
# u  1
# w  2
# $

def countLetters(sentence):
    dict ={}
    sentence=sentence.lower()
    for letter in set(sentence):
        if str(letter).isalpha():
            dict[letter]=sentence.count(letter)
    print(dict)
    for key,value in sorted(dict.items()):
        print(key,"\t",value)


countLetters("ThiS is String with Upper and lower case Letters.")

