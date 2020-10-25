myList = [1, 2, 3, 4, 5, 6, 7]
listSum = 0
for num in myList:
    listSum = listSum + num
    print(listSum)

print("------------")
print(listSum)
print("------------")

myList2 = [(1, 2), (3, 4), (5, 6), (7, 8)]
for (a, b) in myList2:
    print((a + b) * a * b)

print("------------")

dic = {"k1": 123, "k2": [1, 3, 5, 7, 9], "k3": {"insideKey": 100}, "k4": ["a", "b", "c"], "k5": 500}
for key, value in dic.items():
    print(value)

print("------------")


# ==========================================================

def lower_from_two_number(a, b):
    if a % 2 == 0 and b % 2 == 0:
        if a < b:
            result = a
        else:
            result = b
    else:
        if a < b:
            result = b
        else:
            result = a

    print(result)


lower_from_two_number(2, 7)


# ========================================================


def from_two_number(a, b):
    if a % 2 == 0 and b % 2 == 0:
        return min(a, b)
    else:
        return max(a, b)


result = from_two_number(200, 700)

print(result)


# ========================================================


def my_text(text):
    wordList = text.split()
    reverse_word_list = wordList[::-1]
    return " ".join(reverse_word_list)


value = my_text(input("Give Input: "))

print(value)
