
translator = {"sir":"matey",
            "hotel":"fleabag inn",
            "student":"swabbie",
            "boy":"matey",
            "madam":"proud beauty",
            "professor":"foul blaggart",
            "restaurant":"galley",
            "your":"yer",
            "excuse":"arr",
            "students":"swabbies",
            "are":"be",
            "lawyer":"foul blaggart",
            "the":"th’",
            "restroom":"head",
            "my":"me",
            "hello":"avast",
            "is":"be"}

def translate(sentence): #1st Solution.
    words = list(sentence)
    phrase = ""
    for word in sentence.lower().split():
        tr_word = translator.get(str(word),"_null_") #translator[str(word)]
        phrase = str(phrase+" "+"".join(str(tr_word)))
    return phrase

print(translate(input("Enter your phrase: ").lower()))

def eng2pirate(sentence): #2nd solution (cleaner than 1st)
    for key in translator:
        while key in sentence:
            sentence = sentence.replace(key,translator.get(key).lower())
    return sentence.capitalize() #Deixa a primeira letra maiúscula.

print(eng2pirate(input("Enter your phrase: ").lower()))

