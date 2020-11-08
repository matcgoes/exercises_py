# Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).
def generatePow2(n):
    d = dict()
    for i in range(1,n+1):
        d[i]=i*i
    return print(d.items())

generatePow2(5)

# Write a Python program to create a dictionary of keys x, y, and z where each key has as value a
# list from 11-20, 21-30, and 31-40 respectively. Access the fifth value of each key from the dictionary.
dicx = {"x": list(val for val in range(11,21))}
dicy = {"y": list(val for val in range(21,31))}
dicz = {"z": list(val for val in range(31,41))}
print(dicx)
print(dicy)
print(dicz)
print(dicx.get("x")[4])
print(dicy.get("y")[4])
print(dicz.get("z")[4])