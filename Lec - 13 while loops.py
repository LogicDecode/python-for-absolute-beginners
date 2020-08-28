# while Loops
# Loops a block of code until a condition is true

# Syntax
# while condition:
#   code to loop

num = 0
while num < 5:
    print(num)
    num = num + 1
else:
    print("num is not less than 5")


# break - breaks out of current closest enclosing loop
# continue - skips the current iteration of the loop and goes to next one
# pass - do nothing

# example of break
mylist = [1, 2, 3, 4, 5, 6, 7, 8]
print("\n\nBreak Loop")
for num in mylist:
    if num == 5:
        break
    print(num)

# else with break
print("\n\nElse with break")
for i in mylist:
    if i == 10:
        break
    print(i)
else:
    print("10 is not in the elements")

# Breaking out of loop
mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("\n\nElse with break")
for i in mylist:
    if i == 10:
        break
    print(i)
else:
    print("10 is not in the elements")

# example of continue
print("\n\nContinue Loop")
for num in mylist:
    if num == 5:
        continue
    print(num)

# example of pass
for i in mylist:
    pass

print("End of Program")
