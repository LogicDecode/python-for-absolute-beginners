from random import shuffle # Importing function shuffle
test = [1,2,3,4,5,6]
shuffle(test) # The list test will be shuffled
print(test)


mycups = [' ', 'O', ' ']

# Function to shuffle the cups order
def shuffle_cups(mycups):
    shuffle(mycups)
    return mycups


print(shuffle_cups(mycups))
print(shuffle_cups(mycups))
print(shuffle_cups(mycups))


# Function to take user input as guess
def user_input():
    cupnum = ''
    while cupnum not in ['0', '1', '2']:
        cupnum = input('Pick a number - 0, 1 or 2 : ')
    return int(cupnum)


# Function to check if the user won
def check_win(mycups, cupnum):
    if mycups[cupnum] == 'O':
        print("Correct!")
    else:
        print("Wrong Answer!")
        print(mycups)

# MAIN GAME CODE
mycups = [' ', 'O', ' ']
mycups = shuffle_cups(mycups)
cupnum = user_input()
check_win(mycups, cupnum)