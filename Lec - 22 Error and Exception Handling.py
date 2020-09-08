# When interacting with a user, or changing environment of program, there are chances of getting a error or exception

# Error and Exception are some event during runtime for which the program was not prepared of and force the program to quit

# Example of Error (Syntax Error)
# if 1 > 2:


# Example of Exception
# num1 = int(input("Enter num 1: "))
# num2 = int(input("Enter num 2: "))
# result = num1 + num2
# print(result)

# Handling Error
# try statement with except

# try:
#     num1 = int(input("Enter num 1: "))
#     num2 = int(input("Enter num 2: "))
#     result = num1 + num2
#     print(result)
# except:
#     print('Wrong Input')


# Using else block
# try:
#     num1 = int(input("Enter num 1: "))
#     num2 = int(input("Enter num 2: "))
#     result = num1 + num2
# except:
#     print('Wrong Input')
# else: 
#     print(result)


# finally block
# try:
#     num1 = int(input("Enter num 1: "))
#     num2 = int(input("Enter num 2: "))
#     result = num1 + num2
# except:
#     print('Wrong Input')
# else: 
#     print(result)
# finally:
#     print("The program completed successfully")

# Catch specific Error
try:
    myfile = open('test', 'r')
    myfile.write('THIS IS TEST')
except SyntaxError:
    print('You have syntax error')
except OSError:
    print('OS ERROR FOUND')
finally:
    print('Program Done')