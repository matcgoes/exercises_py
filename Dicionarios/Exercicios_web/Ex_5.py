#These exercises reffers to dictionary practice, source on:
# https://erlerobotics.gitbooks.io/erle-robotics-learning-python-gitbook-free/content/lists/exercises_list_and_dictionaries.html

#Exercise 1
inventory = {
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'gemstone'],
    'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']
}
inventory['pocket']=['seashell','strange berry','lint']
print(inventory)

inventory['backpack'].sort()
print(inventory)

inventory['backpack'].remove('dagger')
print(inventory)

inventory['gold']=inventory['gold']+50
print(inventory)

#Exercise 2
prices ={"banana": 4,
"apple": 2,
"orange": 1.5,
"pear": 3}

stock=dict()
stock["banana"]= 6
stock["apple"]= 0
stock["orange"] =32
stock["pear"]= 15

for key in sorted(prices):
    print("\n"+key)
    print("price: ",prices[key])
    print("stock: ",stock.get(key,0))

total = 0
for key in sorted(prices):
    total = total + prices.get(key,0)*stock.get(key,0)
    print("Total by far:",total)
print("\nTotal earned: ",total)

#Exercise 3
groceries = ["banana","orange","apple"]
stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

def compute_bill(food):
    total = 0
    for item in food:
        if stock[item] > 0:
            total = total + prices.get(item,0)
            stock[item] = stock[item] - 1 #Here we're updating the stock items
    return total

print(compute_bill((groceries)))
print(stock)

# Exercise 4
lloyd = {
    "name": "Lloyd", 
    "homework": [90.0,97.0,75.0,92.0], 
    "quizzes": [88.0,40.0,94.0], 
    "tests": [75.0,90.0]
}
alice = {
    "name": "Alice",
  "homework": [100.0, 92.0, 98.0, 100.0],
  "quizzes": [82.0, 83.0, 91.0],
  "tests": [89.0, 97.0]
}
tyler = {
    "name": "Tyler",
  "homework": [0.0, 87.0, 75.0, 22.0],
  "quizzes": [0.0, 75.0, 78.0],
  "tests": [100.0, 100.0]
  }


students = [lloyd, alice, tyler]


for name in students:
    print(name.get("name"))
    print("Homeworks: ",name.get("homework"))
    print("Quizzes: ",name.get("quizzes"))
    print("Tests: ",name.get("tests"))


def avg(number_list):
    return float(sum(number_list)/len(number_list))


def get_average(studentdict):
    homework_avg = avg(studentdict["homework"]) #or avg(studentdict.get("homework"))
    quizzies_avg = avg(studentdict["quizzes"])
    tests_avg = avg(studentdict["tests"])
    return float(0.1*homework_avg+0.3*quizzies_avg+0.6*tests_avg)

def get_letter_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

print(get_letter_grade(get_average(lloyd))) #Here we're testing our letter grande function.

def get_class_average(students):
    results = []
    for student in students:
        results.append(get_average(student))
    return avg(results)

print("\nClass average is: ",round(get_class_average(students),2))

print("\nClass letter grade is: ", get_letter_grade(get_class_average(students)))