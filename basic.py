newString = input("Input your string: ")
print(newString)
newList = []
for letter in newString:
    newList.append(letter)
    print(newList)
print("")
myNewList = [letter for letter in newString]
print(myNewList)
print("")
myNewList = [x for x in "Pingpong"]
print(myNewList)
print("")
print(newList)
print("")
num_list = [num ** 2 for num in range(0, 11)]
print(num_list)
print("")
num_list = [num ** 2 for num in range(0, 11) if num % 2 == 0]
print(num_list)
print("")

my_new_list = []
my_list1 = [2, 4, 6, 8]
my_list2 = [1, 100, 1000, 10000]
for x in my_list1:
    for y in my_list2:
        my_new_list.append(x * y)
print(my_new_list)
print("")
my_new_list = [x * y for x in my_list1 for y in my_list2]
print(my_new_list)

# ----------------Python For Loop-----------------------
print("")
tryList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for item in tryList:
    print(item)
print("")

for _ in tryList:
    print("Hello")
print("")

for item in tryList:
    if item % 2 == 0:
        print(f"Even: {item}")
    else:
        print(f"Odd: {item}")
print("")

listSum = 0
for item in tryList:
    listSum = listSum + item
    print(listSum)
print("")

myString = "Hello World"
for letter in myString:
    print(letter)
print("")

myTupList = [(1, 2), (3, 4), (5, 6)]
for tup in myTupList:
    print(tup)
print("")
# Tuple Unpacking
for a, b in myTupList:
    print(a)
    print(b)
print("")

longTupList = [(11, 22, 33,), (44, 55, 66), (77, 88, 99)]
for a, b, c in longTupList:
    print(a, b)
    print(c)
print("")

newDic = {"K1": 10, "K2": 20, "K3": 30}
for key in newDic:
    print(key)
print("")

for key in newDic.items():
    print(key)
print("")

for key, value in newDic.items():
    print(value)
print("")

for key in newDic.values():
    print(key)
print("")

print("---------------------------------------------")

# ----------------Python While Loop-----------------------
v = 0
while v < 5:
    print(f"Current value is {v}")
    v = v + 1
else:
    print("Now Current value is not < 5")

print("---------------------------------------------")
# ----------------Python Break, Continue, Pass-----------------------
x = [1, 2, 3, 4, 5]
for item in x:
    pass
print("Nothing Here")

newString = "LUKAPONG"
for letter in newString:
    if letter == "A":
        continue
    print(letter)
print("")
newString = "LUKAPONG"
for letter in newString:
    if letter == "P":
        break
    print(letter)
print("")

v = 0
while v < 7:
    if v == 5:
        break
    print(f"Current value is {v}")
    v += 1

print("---------------------------------------------")
# ----------------Some Operations-----------------------
# range(start, stop, step)
newList = [1, 2, 3]
for item in range(5):
    print(item)
print("")
for item in range(0, 7):
    print(item)
print("")
for item in range(1, 10, 3):
    print(item)
print("")
print(list(range(0, 11, 2)))

index_count = 0
for letter in "abcde":
    print("At index {} the letter is {}".format(index_count, letter))
    index_count += 1
print("")
index_count = 0
for letter in "zyxwv":
    print(f"At index {index_count} the letter is {letter}")
    index_count += 1
print("")

index_count = 0
word = "abcdefg"
for letter in word:
    print(word[index_count])
    index_count += 1
print("")

for item in enumerate(word):
    print(item)
print("")
for index, letter in enumerate(word):
    print(index)
    print(letter)
    print("")

list1 = [1, 2, 3, 4, 5]
list2 = ["a", "b", "c", "d", "e"]
for item in zip(list1, list2):
    print(item)
print(list(zip(list1, list2)))

check = "x" in ["x", "y", "z"]
print(check)

luka = {"man": 305}
print(345 in luka.keys())

numList = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print(min(numList))
print(max(numList))

from random import shuffle
from random import randint

numList = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
shuffle(numList)
print(numList)
randomNumber = randint(0, 100)
print(randomNumber)

print("---------------------------------------------")

for x in ['A', 'B', 'C']:
    print(x + 'A')

print("---------------------------------------------")
# ----------------Python List-----------------------
myList = ["one", "two", "three", "four"]
yourList = ["red", "blue", "pink"]
newList = myList + yourList
print(newList)
print(len(newList))

# Adding item into last of a list
appendItem = newList.append("book")
print(newList)
print(appendItem)

# Removing item from last of a list
poppedItem = newList.pop()
print(newList)
print(poppedItem)

# Removing list item with index number
removedItem = newList.pop(0)
print(newList)
print(removedItem)

letterList = ['a', 'e', 'x', 'z', 'n', 'k', 'h', 'd']
numberList = [4, 2, 5, 1, 3, 7, 6]
print(letterList)
print(numberList)
letterList.sort()
numberList.sort()
print(letterList)
print(numberList)
letterList.reverse()
numberList.reverse()
print(letterList)
print(numberList)

print("---------------------------------------------")

# ----------------Python Dictionary-----------------------
myDictionary = {"Book": "$3.5", "Pen": "$0.5", "Pencil": "$.25"}
print(myDictionary)
print(myDictionary["Book"])

dic = {"k1": 123, "k2": [1, 3, 5, 7, 9], "k3": {"insideKey": 100}, "k4": ["a", "b", "c"], "k5": 500}
print(dic)
print(dic["k1"])
print(dic["k2"])
print(dic["k2"][2])
print(dic["k3"])
print(dic["k3"]["insideKey"])
print(dic["k4"])
print(dic["k4"][0])
print(dic["k4"][0].upper())
print(dic.keys())
print(dic.values())
print(dic.items())

print("---------------------------------------------")

# ----------------Python Tuple-----------------------
myTuple = ("a", "b", "c", "a", "b", "d")
print(myTuple)
print(myTuple[2])
print(myTuple.count("a"))
print(myTuple.index("d"))
print("---------------------------------------------")

# ----------------Python Tuple-----------------------
mySet = set()
mySet.add(1)
print(mySet)
mySet.add(2)
print(mySet)
mySet.add(2)
print(mySet)
mySet.add(3)
print(mySet)

print("---------------------------------------------")
age = int(input("Enter your age: "))
if age <= 0:
    print("You entered a wrong age, try again")
elif age < 13:
    print("Hello Kid")
elif age < 18:
    print("Hello Teen")
else:
    print("Hello Adult")

print("---------------------------------------------")

data = int(input("Times you want to be greeted: "))
i = 1
while i <= data:
    print("Hello")
    i = i + 1

print("---------------------------------------------")

number = float(input("Enter your number: "))
result = number * 0.15
str_result = str(result)
# Formatting in Python
print("Your result is " + str_result)
print("Your result is {}".format(result))
print("Your result is {r}".format(r=result))
print("Your result is {r:1.2f}".format(r=result))
print(f"Your result is {result}")

print("---------------------------------------------")

name = input("What is your name: ")
condition = ""
if age <= 0:
    print("You entered a wrong age, try again")
elif age < 13:
    condition = "Kid"
elif age < 18:
    condition = "Teen"
else:
    condition = "Adult"
print(f"Hello {name} good day! You are {condition}.\nYour age is {age} now.")
