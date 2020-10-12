print('This is a String')
print("This is also a String")

name = "RHYTHM BHIWANI"
print(type(name))

# Indexing
string = "abcdefghijkl"
print(string[0], string[1], string[2])
print(string[-1], string[-2]) # Reverse Indexing

# Slicing [start:stop:step] - stop in not included
print(string[:]) # Print complete string
print(string[2:]) # Start with index 2 till end
print(string[:2]) # From starting till index 1
print(string[0:10:2]) # Moves from index 0 to 9 and prints alternative charachters


# Length of string
print(len('RHYTHM BHIWANI')) # 14 (Also includes space)

# Repeat String
print('ha'*10)

# Methods of String
name = 'Rhythm Bhiwani'
print(name.upper()) # Capitalize each letter
print(name.lower()) # Lower Case each letter

# Split String [Convert to List]
print(name.split()) # Splits by space character
print(name.split('h')) # Splits by h character

# Concatination
name = 'Rhythm'
age = 21
print('Hello Mr. '+name+'. You are '+str(age)+' years old')

print('Hello Mr. {}. You are {} years old'.format(name,age))

print('Hello Mr. %s. You are %d years old' %(name,age))

print(f'Hello Mr. {name}. You are {age} years old')
