# What is List
# A data type to store multiple values together
# Represented by Square Brackets [ ]

# Making empty list
empty_list = []
epmty_list2 = list()

# Making list with with data in it
mylist = ['a', 'b', 'c', 'd', 'e']
user_data = ["Rhythm", 20, 69.99] # List with different data types

# List Indexing
print("Name: {}".format(user_data[0]))
print("Age: {}".format(user_data[1]))
print("Percentage: {}".format(user_data[2]))

# List Slicing
print(mylist[:3])
print(mylist[3:])
print(mylist[1:4])
print(mylist[::2])

# Length
print(len(mylist))

# List Concatination
a = ['a', 'b', 'c']
b = [1, 2, 3]
print(a + b)

# Changing Values
mylist = ['ONE', 'TWO', 'THREE']
print(mylist)

mylist[0] = 'ONLY ONE'
print(mylist)

# Adding new element to list
mylist.append('FOUR') # adds the element at the end
print(mylist)

mylist.insert(1, 'NEW ELEMENT') # add the element at index 1
print(mylist)

list2 = ['FIVE', 'SIX']
mylist.append(list2)
print(mylist)

mylist.extend(list2)
print(mylist)

# Removing Element

mylist.pop() # removes the last element
print(mylist)

mylist.pop(1) # removes the element at index 1
print(mylist)

mylist.remove('ONLY ONE') # removes the element 'ONLY ONE'
print(mylist)

# Clear the whole list
mylist.clear()
print(mylist)

# Sorting List
mylist = [ 5, 9 , 1 , 9 , 5 , 8 , 4 , 3 , 9]
print("Unsorted: ",mylist)
mylist.sort()
print("Sorted: ", mylist)

# Reverse the list
mylist.reverse()
print("Reversed: ",mylist)

# Count Elements
print(mylist.count(9))

# Nested List
mylist = [ [1, 2] , ['a', 'b'] ]
print(mylist[0])
print(mylist[0][0])


# Task
mylist1 = [ ["Hello" , "Logic"] , ["There", "Decode"] ]
# Need Output as following in one line
# Hello There, Logic Decode