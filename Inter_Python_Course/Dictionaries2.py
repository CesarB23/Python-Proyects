from random import sample

from cv2 import add


keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
dict1 = dict()

for i in range(len(keys)):
    dict1.update({keys[i]: values[i]})
print(dict1)

dict1 = dict(zip(keys,values))
print(dict1)
 
dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

dict1.update(dict2)
print(dict1)

sampleDict = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}
print(sampleDict["class"]["student"]["marks"]["history"])

employees = ('Kelly', 'Emma')
print(type(employees))
defaults = {"designation": 'Developer', "salary": 8000}
res = dict.fromkeys(employees, defaults)
print(res)
print(res["Kelly"])


sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}

keys = ["name", "salary"]

dict3 = {k: sample_dict[k] for k in keys}
print(dict3)

res = dict()

for k in keys:
    # add current key with its va;ue from sample_dict
    res.update({k: sample_dict[k]})
print(res)

sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}

# Keys to remove
keys = ["name", "salary"]

# for key in keys:
#     print(key)
#     if sample_dict[key]:
#        sample_dict.pop(key)
# print(sample_dict)

for key in keys:
    sample_dict.pop(key)
print(sample_dict)
lst= []
sample_dict = {'a': 100, 'b': 200, 'c': 300}
x,y,z = sample_dict.values()
for i in sample_dict.values():
    lst.append(i)
if 200 in lst:
    print(200, "present in dict")

sample_dict = {'a': 100, 'b': 200, 'c': 300}
if 200 in sample_dict.values():
    print('200 present in a dict')

sample_dict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"
}

sample_dict['location'] = sample_dict.pop('city')
print(sample_dict)

sample_dict = {
  'Physics': 82,
  'Math': 65,
  'history': 75
}
lst= []
for i in sample_dict.values():
    lst.append(i)
    lst.sort()
print(lst[0])

print(min(sample_dict, key=sample_dict.get))

sample_dict = {
    'emp1': {'name': 'Jhon', 'salary': 7500},
    'emp2': {'name': 'Emma', 'salary': 8000},
    'emp3': {'name': 'Brad', 'salary': 500}
}
print(sample_dict["emp3"])
sample_dict["emp3"]["salary"] = 8500
print(sample_dict)

person_details = {"name": "Jessa", "country": "USA", "telephone": 1178}

# set default value if key doesn't exists
person_details.setdefault('state', 'Texas')
person_details.setdefault("zip")
person_details.setdefault('country', 'Canada')
print(person_details)

for key, value in person_details.items():
    print(key, ':', value)

    person = {'name': 'Jessa', 'country': 'USA', 'telephone': 1178, 'weight': 50, 'height': 6}

# Remove last inserted item from the dictionary
deleted_item = person.popitem()
print(deleted_item)  # output ('height', 6)
# display updated dictionary
print(person)  
# Output {'name': 'Jessa', 'country': 'USA', 'telephone': 1178, 'weight': 50}

# Remove key 'telephone' from the dictionary
deleted_item = person.pop('telephone')
print(deleted_item)  # output 1178
# display updated dictionary
print(person)  
# Output {'name': 'Jessa', 'country': 'USA', 'weight': 50}

# delete key 'weight'
del person['weight']
# display updated dictionary
print(person)
# Output {'name': 'Jessa', 'country': 'USA'}

# remove all item (key-values) from dict
person.clear()
# display updated dictionary
print(person)  # {}

# Delete the entire dictionary
del person

# address dictionary to store person address
address = {"state": "Texas", 'city': 'Houston'}

# dictionary to store person details with address as a nested dictionary
person = {'name': 'Jessa', 'company': 'Google', 'address': address}

# Display dictionary
print("person:", person)

# Get nested dictionary key 'city'

print("City:", person['address']['city'])
print("Personal Details\n")
for key,value in person.items():
    if key == 'address':
        print("Person Address\n")
        for nested_keys,nested_values in value.items():
            print(nested_keys, ":" ,nested_values)
    else:
        print(key, ":", value)


d1 = {'a': 10, 'b': 20, 'c': 30}
d2 = {'d': 40, 'e': 50, 'f': 60}
d3 = {**d1,**d2}
print(d3)

student = {1: {'name': 'Emma', 'age': '27', 'sex': 'Female'},
           2: {'name': 'Mike', 'age': '22', 'sex': 'Male'}}
print(student[1]["age"])



sampleDict = { 
   "class":{ 
      "student":{ 
         "name":"Mike",
         "marks":{ 
            "physics":70,
            "history":80
         }
      }
   }
}
print(sampleDict['class']['student']['marks']['history'])

student = {
  "name": "Emma",
  "class": 9,
  "marks": 75
}
student.popitem("marks")
print(student)