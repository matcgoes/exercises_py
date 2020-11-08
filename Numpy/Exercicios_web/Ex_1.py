# Source on: https://pynative.com/python-numpy-exercise/

import numpy as np

# Question 1: Create a 4X2 integer array and Prints its attributes
# Note: The element must be a type of unsigned int16. And print the following Attributes: –
# The shape of an array.
# Array dimensions.
# The Length of each element of the array in bytes.

a = np.random.randint(0,10,(4,2))
a = a.astype('int16')
print('Array shape: {}'.format(a.shape))
print('Array dimension: {}'.format(a.ndim))
print('Element bytes: {}'.format(a.itemsize))

# Question 2: Create a 5X2 integer array from a range between 100 to 200 such that the difference between each element is 10
b = np.arange(100,200,10)
b.resize(5,2)
print(b)

# Question 3: Following is the provided numPy array. return array of items in the third column from all rows
sampleArray = np.array([[11 ,22, 33], [44, 55, 66], [77, 88, 99]])

c = sampleArray[:,2]
print(c)

# Question 4: Following is the given numpy array return array of odd rows and even columns
sampleArray = np.array([[3 ,6, 9, 12], [15 ,18, 21, 24], 
[27 ,30, 33, 36], [39 ,42, 45, 48], [51 ,54, 57, 60]])

# odd = sampleArray[sampleArray%2!=0] ME CONFUNDI! NAO E ESSA A SOLUCAO
# even = sampleArray[sampleArray%2==0]

d = sampleArray[::2,1::2]
print(d)


# Question 5: Add the following two NumPy arrays and Modify a result array by calculating the square of each element
arrayOne = np.array([[5, 6, 9], [21 ,18, 27]])
arrayTwo = np.array([[15 ,33, 24], [4 ,7, 1]])

sumArray = (arrayOne + arrayTwo)**2
print(sumArray)


# Question 6: Split the array into four equal-sized sub-arrays
# Note: Create an 8X3 integer array from a range between 10 to 34 such that the difference between each element is 1 
# and then Split the array into four equal-sized sub-arrays.

e = np.arange(10,34)
e = e.reshape(8,3)
e = np.split(e,4)
print(e)

# Question 7; Sort following NumPy array
# 7.1- by the second row and
# 7.2-by the second column

sampleArray = np.array([[34,43,73],[82,22,12],[53,94,66]])
print(sampleArray)

sortArrayByRow = sampleArray[:,sampleArray[1,:].argsort()]

print(sampleArray)

# Question 8: Following is the 2-D array. Print max from axis 0 and min from axis 1
sampleArray = np.array([[34,43,73],[82,22,12],[53,94,66]])

# a_min = np.array([min(i) for i in sampleArray])
# a_max = np.array([max(i) for i in sampleArray])

minOfAxisOne = np.amin(sampleArray, 1) 
print("Printing amin Of Axis 1")
print(minOfAxisOne)

maxOfAxisOne = np.amax(sampleArray, 0) 
print("Printing amax Of Axis 0")
print(maxOfAxisOne)

# print(a_min)
# print(a_max)

# Question 9: Following is the input NumPy array delete column two and insert following new column in its place.
sampleArray = np.array([[34,43,73],[82,22,12],[53,94,66]]) 
newColumn = np.array([[10,10,10]])

print(sampleArray)
sampleArray[:,1] = newColumn
print(sampleArray)