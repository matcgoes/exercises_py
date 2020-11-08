#The following exercises can be found on: https://pynative.com/python-tuple-exercise-with-solutions/

#Exercise 1 - Reverse the following tuple
aTuple = (10, 20, 30, 40, 50)
print(aTuple[::-1])


#Exercise 2 - Access value 20 from the following tuple
aTuple = ("Orange", [10, 20, 30], (5, 15, 25))
print(aTuple[1][1])


#Exercise 3 - Create a tuple with single item 50
aTuple = (50,) #If you want to create a tuple with a single value, you need to add comma after the value. Otherwise it will return a value
aTuple_2 = (50) # It's not a tuple but a int value.
print(type(aTuple))
print(type(aTuple_2))


#Exercise 4 - Unpack the following tuple into 4 variables
aTuple = (10, 20, 30, 40)
a,b,c,d = aTuple
print(a)
print(b)
print(c)
print(d)


#Exercise 5 - Swap the following two tuples
tuple1 = (11, 22)
tuple2 = (99, 88)
tuple1, tuple2 = tuple2, tuple1
print(tuple1)
print(tuple2)


#Exercise 6 - Copy element 44 and 55 from the following tuple into a new tuple
tuple1 = (11, 22, 33, 44, 55, 66)
new_tuple = tuple1[tuple1.index(44)], tuple1[tuple1.index(55)]
#new_tuple = tuple1[3:5]  #This is an alternate way to do it.
print(new_tuple)


#Exercise 7 - Modify the first item (22) of a list inside a following tuple to 222
tuple1 = (11, [22, 33], 44, 55)
tuple1[1][0] = 222
print(tuple1)


#Exercise 8 - Sort a tuple of tuples by 2nd item
tuple1 = (('a', 23),('b', 37),('c', 11), ('d',29))
# tuple2 = tuple(sorted(list(tuple1),key=lambda v: v[1])) #One-step solution
print(tuple2)
list_0 = list(tuple1)
print(list_0)
list_0.sort(key=lambda v: v[1])
print(list_0)
tuple_ord = tuple(list_0)
print(tuple_ord)

#Exercise 9 - Counts the number of occurrences of item 50 from a tuple
tuple1 = (50, 10, 60, 70, 50)
print(tuple1.count(50))

#Exercise 10 - Check if all items in the following tuple are the same
tuple1 = (45, 45, 45, 45)
print(bool(len(set(tuple1))==1))

def check_values(tuplesample): #This is another solution.
    return all(i == tuplesample[0] for i in tuplesample)
print(check_values(tuple1))