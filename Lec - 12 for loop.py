# Print Table of 2
print("Table of 2 manually")
print("2 x 1 = 2")
print("2 x 2 = 4")
print("2 x 3 = 6")
print("2 x 4 = 8")
print("2 x 5 = 10")
print("2 x 6 = 12")
print("2 x 7 = 14")
print("2 x 8 = 16")
print("2 x 9 = 18")
print("2 x 10 = 20")

# Do it with a for loop
print("\n\nTable of 2 with for loop")
for i in range(1, 11):
    print("2 x {} = {}".format(i, 2*i))

# iterable objects: list, dict, string, range

# Iterating a list
print("\n\nIterating a list")
mylist = [1, 2, 3, 4, 5, 6, 7, 8]
for item in mylist:  # Here item is a variable name and can be changed
    print(item)  # prints each list item

for item in mylist:
    print("Logic Decode")  # It is not compulsary to use item variable


# Checking even number
print("\n\nEven Numbers")
for num in mylist:
    if num % 2 == 0:  # True if number is even
        print(num)
    else:
        print('{} is odd'.format(num))

# Sum of all numbers in list
print("\n\nSum of numbers")
sum = 0
for num in mylist:
    sum = sum + num
print(sum)


# Iterating string
print("\n\nIterating String")
mystring = "Logic Decode"
for letter in mystring:
    print(letter)

for letter in "Logic Decode":
    print(letter)

# If we dont wan't to use the variable

for _ in "Logic Decode":
    print('Hey')

# Iterating Tuple
print("\n\nIterating Tuple")
mytup = (1, 2, 3)
for i in mytup:
    print(i)

# Tuple Unpacking
print('\n\nTuple Unpacking')
a,b = (1,2)
print(a,b)


mylist = [(1, 2), (3, 4), (5, 6), (7, 8)]
print("Length of mylist:", len(mylist))

for item in mylist:
    print(item)


# Tuple unpacked
for (a, b) in mylist:  # Brackets are optional
    print(a, "+", b, "=", a+b)


# Iterating Dictionary
mydict = {'A': 1, 'B': 2, 'C': 3, 'D': 4}
for key in mydict:
    print(key)

print(mydict.items())

for tup in mydict.items():
    print(tup)

# Tuple unpacked
for key, value in mydict.items():
    print(key, "=>", value)


for i in range(0,5):
    print(i)
else:
    print("My loop is completed")