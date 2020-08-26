# Specify Conditions
password = input('Enter password: ')
print(password == "123")

# Syntax of if
# if conditions:
    # Code to run if condition is true

if password == "123":
    print("Login")

# else Condition
if password == "123":
    print("Login")
else:
    print("Password not correct")

# Percentage to Grade Example (Ladder if)
per = int(input('Enter Percentage: '))
if per > 90:
    print('A')
elif per > 80:
    print('B')
elif per > 70:
    print('C')
elif per > 60:
    print('D')
else:
    print('E')

# Nested if
card = input('Enter correct: ')
if card == "correct":
    pin = input('Enter PIN: ')
    if pin == "1234":
        print("PIN correct")