# Checking even number
num1 = 10
num2 = 15

# Checking num1
if num1 % 2 == 0:
    print(True)
else:
    print(False)

# Checking num2
if num2 % 2 == 0:
    print(True)
else:
    print(False)

# Creating function to check even number
def check_even(num):
    if num % 2 == 0:
        print(True)
    else:
        print(False)

check_even(num1)
check_even(num2)

