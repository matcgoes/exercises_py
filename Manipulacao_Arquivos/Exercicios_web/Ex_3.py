#File exercises from: https://www.w3resource.com/python-exercises/file/

# 2. Write a Python program to read first n lines of a file.
def readLinesfrom(file,n):
    with open(file,'r') as f:
        listlines = f.readlines()
        for line in range(n):
            print(listlines[line])

readLinesfrom("practiceblurb.txt",1)



# 4. Write a Python program to read last n lines of a file.
def readLastLines(file,n):
    with open(file,'r') as f:
        listrows = f.readlines()
        for line in range(len(listrows)-n,len(listrows)):
            print(listrows[line].rstrip())

# readLastLines('practiceblurb.txt',3)


# 8. Write a python program to find the longest words.
def findLongWord(file):
    with open(file,'r') as f:
        dic = {}
        words = f.read().lower().split()
        for word in set(words):
            dic[word] = len(word)
        keys = list(dic.keys())
        values = list(dic.values())
        max_ind = values.index(max(values))
        return keys[max_ind]

print(findLongWord('practiceblurb.txt'))

def longest_word(filename):
    with open(filename, 'r') as infile:
        words = infile.read().split()
    max_len = len(max(words, key=len))
    return [word for word in words if len(word) == max_len]

print(longest_word('practiceblurb.txt'))


# 16. Write a Python program to assess if a file is closed or not.
def isClosed(file):
    return file.closed

file = 'practiceblurb.txt'
with open(file,'r') as f:
    print(isClosed(f))
print(isClosed(f))


# 17. Write a Python program to remove newline characters from a file.
def remove_newlines(file):
    with open (file,'r') as f:
        flist = f.readlines()
        return [l.rstrip("\n") for l in flist]

print(remove_newlines('practiceblurb.txt'))


# 19. Write a Python program to extract characters from various text files and puts them into a list.
import glob

def charactersList(filelist):
    charlist = []
    for file in filelist:
        with open(file,'r') as f:
            charlist.append(f.read())
    return charlist

filelist_txt = glob.glob("words*.txt")
print(charactersList(filelist_txt))