# Taking Input in Python
name = input()
print(name)

name = input('Enter your Name: ') # Provide a prompt to user
print(name)

# Data Type Conversion
# Example
a = input() # Suppose 5
b = input() # Suppose 10
print(a+b) # Then output will be 510 not 15 as these are string inputs

# String to int
a = int(a)
b = int(b)
print(a+b) # 15 this time

# Convert input directly to int
num = int(input())
print(type(num))

# Comparison Operators
# is equal to (==)
print(5 == 5) # True

print('rhythm' == 'rhythm') # True

print('rhythm' == 'Rhythm') # False as it is case - sensitive

password = input('Enter your password: ')
print(password == '123abc') # True if password matches 123abc

print(10.0 == 10) # True - float and int can be compared

# not equals to (!=)
print(10 != 10) # False

print(10 != 11) # True

# Greater than and less than
per = float(input('Enter Percentage: '))
print(per > 90) # True if percentage is greater than 90
print(per < 90) # True if percentage is less than 90

print(per >= 90) # True if percentage is greater than or equals 90
print(per <= 90) # True if percentage is less than or equals 90

# Chaining Operators
print(1 < 2 < 3) # True

# Logical Operators
# and - both conditions should be correct
print(1 < 2 and 2 < 3) # True
print(1 < 2 and 2 > 3) # False

username = input('Enter Username: ')
password = input('Enter Password: ')
print(username == 'rhythm' and password == '123')

# or - any of 2 conditions should be true
print(1 < 2 or 2 > 3) # True as 1 < 2
print(1 > 2 or 2 > 3) # False as both are false

# not - true -> false and false -> true
print(1 < 2) # True
print(not 1 < 2) # False

