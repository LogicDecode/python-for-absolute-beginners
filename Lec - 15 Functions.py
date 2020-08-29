# Functions are used to make reusable code
# functions are defined using "def" keyword and called using the brackets ()

# Syntax
# Defining a function
def name_of_function():
    # This is the code to run when function is called
    print("Hi I am a function")

# Calling a function
name_of_function()


# Getting parametes in function
def name_of_function(name):
    print("Hello there", name)

name_of_function("Rhythm") # pass the value to parameter

# Multi parameter function
def name_of_function(name, channel_name):
    print("Hello there", name)
    print("Welcome to", channel_name)

name_of_function("Rhythm", "Logic Decode")

# Until now only we have given parameters to the function but the function didn't gave us back anything
# To get something back from the function we use return keyword

# Function to add 3 numbers
def sum_of_3(num1, num2, num3):
    answer = num1 + num2 + num3
    return answer

myanswer = sum_of_3(1, 2, 3)
print(myanswer)

# Giving Default value as parameter
def say_hello(name="Default"):
    print("Hello", name)

say_hello("RHYTHM")
say_hello()

# The function ends after returning
def myfunc():
    print("HI THIS IS MYFUNC")
    return "MYFUNC"

print(myfunc())

def myfunc():
    return "MYFUNC"
    print("HI THIS IS MYFUNC")

print(myfunc())