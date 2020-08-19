# Unorderd Map of Key Value Pairs
# Represented by { }

# Making Empty Dict
mydict = {}
mydict = dict()

# Making dict with data
mydict = {
    "name": "rhythm",
    "age": 20,
    "channel": "Logic Decode"
}

# Accessing value of dict
print(mydict["name"])
print(mydict["age"])

# Insert Element into dict
mydict["language"] = "Python"
print(mydict)

# Updating Element from dict
mydict["language"] = "Python3"
print(mydict)

# Nested dict
newdict = {
    "company": ['Google', 'FB'],
    "price": {
        "apple": 50,
        "grapes": 45.5
    }
}
print(newdict)
print(newdict["company"][0])

# deleting item from dict
del newdict['company']
print(newdict)

# Get all Keys
print(mydict.keys())

# Get all Values
print(mydict.values())

# Get all items
print(mydict.items())

# Task
mydict = {
    "name": "Logic Decode",
    "subs": {
        "july": 0,
        "aug": 50
    }
}
# Increase value of subs in month of aug to 100