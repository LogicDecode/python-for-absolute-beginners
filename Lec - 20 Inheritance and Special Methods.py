# Use a base class to derive attributes and methods to child class

# Creating Base class
class Animal:
    
    def __init__(self):
        print("HEY I AM AN ANIMAL")

    def move(self):
        print("I AM MOVING")

    def eat(self):
        print("I AM EATING")


# Object of Base Class
myanimal = Animal()
myanimal.move()


# Creating Derived Class
class Snake(Animal):

    def __init__(self):
        super().__init__()
        print("I AM A SNAKE")

  
# Creating Objecet of Child Class
mysnake = Snake()
mysnake.eat()


# Redefining Method
class Snake(Animal):

    def __init__(self):
        super().__init__()
        print("I AM A SNAKE")

    def eat(self):
        print("I AM EATING A CHUHAA")

    def say(self):
        print("HIISSSSSSSSS")

mysnake = Snake()
mysnake.eat()
mysnake.move()
mysnake.say()


# Special Methods

mylist = [1,2,3]
len(mylist)
print(mylist)

# print(len(mysnake)
print(mysnake)

class Snake(Animal):

    def __init__(self):
        super().__init__()
        print("I AM A SNAKE")

    def eat(self):
        print("I AM EATING A CHUHAA")

    def say(self):
        print("HIISSSSSSSSS")

    def __str__(self):
        return "This is a snake object"

    def __len__(self):
        return 2
        


mysnake = Snake()

print(len(mysnake))
print(mysnake)