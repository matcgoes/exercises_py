# The exercises below were taken from : 
# https://raw.githubusercontent.com/zhiwehu/Python-programming-exercises/master/100%2B%20Python%20challenging%20programming%20exercises.txt

# Question 8
# Level 2

# Question:
# Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated
#  sequence after sorting them alphabetically.
# Suppose the following input is supplied to the program:
# without,hello,bag,world
# Then, the output should be:
# bag,hello,without,world

def sortCommaString(s):
    lt = s.split(',')
    lt.sort()
    return ','.join(lt)

print(sortCommaString("dog,armor,bee,kitchen"))



