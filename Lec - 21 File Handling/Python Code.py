# Using Files To Store or Get Data

# Reading a file - Gives Error if file does not exist
myfile = open('file1.txt')
data = myfile.read()
print(data)
myfile.close()


# Opening a file in Write (Overwrites) mode, creates if file not exist
myfile = open('./file2.txt', 'w')
myfile.write("HEY THIS IS LOGIC DECODE")
myfile.close()


# Opening file in append mode - does not overwrite
myfile = open('./file2.txt', 'a')
myfile.write("\nTHIS IS THE 2ND LINE")
myfile.close()


# Opening a file temporarly
with open('./file2.txt') as myfile:
    print(myfile.read())
