class Dog:

    def __init__(self, myBreed, name, color):
        self.breed = myBreed
        self.name = name
        self.color = color


my_dog = Dog(myBreed="Lab", name="Tomi", color="Black")
print(my_dog.breed)
print(my_dog.name)
print(my_dog.color)
