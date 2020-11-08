# Here are some basic JSON exercises. Source on: https://pynative.com/python-json-exercise/
# LET'S GET STARTED!

import json 

# Question 1: Convert the following data into JSON format
data = {"key1" : "value1", "key2" : "value2"}
jsonData = json.dumps(data)
print(jsonData)
# with open("arq1.json","w") as firstfile:
#     json.dump(data,firstfile)

# Question 2: Access the value of key2 from the following JSON
sampleJson = """{"key1": "value1", "key2": "value2"}"""

data = json.loads(sampleJson)
print(data)
print(data.get("key2"))


# Question 3: PrettyPrint following JSON data
sampleJson = {"key1" : "value2", "key2" : "value2", "key3" : "value3"}

PrettyPrintJson = json.dumps(sampleJson,indent=2,separators=(","," = "))
print(PrettyPrintJson)


# Question 4: Sort JSON keys in Python and write it into a file
sampleJson = {"id" : 1, "name" : "value2", "age" : 29}

print("Starting writing a JSON file...")
with open("sampleJson.json","w") as jsonfile:
    json.dump(sampleJson,jsonfile,indent=4,sort_keys=True)
    print(jsonfile.closed)
print("Done writing JSON file!")
print(jsonfile.closed)


# Question 5: Access the nested key ‘salary’ from the following JSON
sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payble":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""

data = json.loads(sampleJson)
print(data['company']['employee']['payble']['salary'])
print(data.get('company').get('employee').get('payble').get('salary'))


# Question 6: Convert the following Vehicle Object into JSON
#--------Para se realizar esse exercício, precisamos aprender CLASSES antes!!!!-------
class Vehicle:
    def __init__(self, name, engine, price):
        self.name = name
        self.engine = engine
        self.price = price

vehicle = Vehicle("Toyota Rav4", "2.5L", 32000)


# Question 7: Convert the following JSON into Vehicle Object
sampleJson = { "name": "Toyota Rav4", "engine": "2.5L", "price": 32000 }


# Question 8: Check whether following json is valid or invalid. If Invalid correct it
# sampleJson = {"company":{"employee":{"name":"emma", "payble":{"salary":7000 "bonus":800}}}}
# echo sampleJson | python -m json.tool

sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payble":{ 
            "salary":7000
            "bonus":800
         }
      }
   }
}"""

#O erro está na falta da "," após o "7000" na chave "salary".
def validateJson(jsonfile):
    try:
        json.loads(jsonfile)
    except ValueError as err:
        return False
    return True

isValid = validateJson(sampleJson)
print(isValid)


# Question 9: Parse the following JSON to get all the values of a key ‘name’ within an array
sampleJson = """[ 
   { 
      "id":1,
      "name":"name1",
      "color":[ 
         "red",
         "green"
      ]
   },
   { 
      "id":2,
      "name":"name2",
      "color":[ 
         "pink",
         "yellow"
      ]
   }
]"""

data = json.loads(sampleJson)
value = [dic.get("name") for dic in data]
print(value)

