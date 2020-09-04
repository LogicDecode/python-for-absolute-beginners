# OOPS - Object-Oriented Prograaming
# Used to group similar data together

# Group attributes and methods in a class
# An instance of class is called object
# Methods are like functions but they work on the specific object

# Example of Class Person with properties or data

class Person:
    name = "Rhythm"
    age = 20
    gender = "Male"


# Creating object of class Person
person1 = Person()

# Accessing attributes of person1
print(person1.name)
print(person1.age)
print(person1.gender)


# Class with constructor
class Person:
    name = "Rhythm"
    age = 20
    gender = "Male"

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender


# Creating Object with constructor values
person2 = Person("Bill Gates", 64, "Male")

# Accessing attributes of person2

print(person2.name)
print(person2.age)
print(person2.gender)


# Creating Class with Methods

class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def giveIntro(self):
        print("Hey, I'm {}, my age is {}, and I am a {}".format(self.name, self.age, self.gender))


# Creating person3 and calling a method
person3 = Person("Erica Fernandes", 27, "Female")
person3.giveIntro()