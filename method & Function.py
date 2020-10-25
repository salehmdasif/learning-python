myList = [1, 2, 3, 4]
# myList.append(5)
print(myList)
myList.pop()
print(myList)
myList.insert(0, 0)
print(myList)


def say_hello(name="Name"):
    """
    Saying Hello
    :return:
    """
    return "hello " + name


greetings = say_hello("Adam")
print(greetings)


def add_function(n1, n2):
    """
    Adding Numbers
    :return:
    """
    return n1 + n2


result = add_function(45, 78)
print(result)


# Find out if the word "dog" is in a string
def dog_check(string):
    if "dog" in string.lower():
        return True
    else:
        return False


check = dog_check("My cat is cute")
print(check)


# ------- the condition is itself a boolean -------
def dog_check(string):
    return "dog" in string.lower()


check = dog_check("My dog is cute")
print(check)


def pig_latin(word):
    """
    If word starts with a vowel, ay to end.
    If word does not start with vowel, put first letter at the end, then add ay.
    :return:
    """
    word = input("Input Word: ")
    first_letter = word[0]
    vowel = "aeiou"
    # checking vowel
    if first_letter.lower() in vowel:
        pig_word = word + "ay"
    elif " " in word:
        return "Please input just a word"
    else:
        pig_word = word[1:] + first_letter + "ay"
    return pig_word


print("Pig Word: " + pig_latin("hello"))


# --------------------------------------------------------------------

def my_function(a, b, c):
    # Returns 5% of the sum of a & b
    return sum((a, b, c)) * 0.05


print(my_function(440, 660, 300))


def my_new_function(*args):
    print(args)
    for items in args:
        print(items)
    # Returns 5% of the sum of the multiple values
    return sum(args) * 0.05


print(my_new_function(440, 660, 300, 500, 700))


# --------------------------------------------------------------------

def my_k_function(**kwargs):
    print(kwargs)
    if "fruit" in kwargs:
        print("My fruit of choice is {}".format(kwargs["fruit"]))
    else:
        print("No fruit here")


my_k_function(Study="book", vegitable="lettuce", fruit="apple")

# --------------------------------------------------------------------


def my_ak_function(*args, **kwargs):
    print("I would like to have {} {}".format(args[0], kwargs["food"]))


my_ak_function(10, 20, 30, food="apple", animal="dog")
