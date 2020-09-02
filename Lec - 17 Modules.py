import math # Importing a module

answer = math.sqrt(64) # Calling a function from that module
print(answer)

print(math.pi) # Using a value stored in the module
print(math.factorial(5))

# Random
import random

print(random.randint(1, 6))

from random import shuffle , randint # Importing Specific Function and values from a module
mylist = [1,2,3,4]
shuffle(mylist)
print(mylist)
print(randint(5,10))

import math as m # Giving Short Name to a module
print(m.pi)

from random import * # Importing all functions and values from a module
print(random())
