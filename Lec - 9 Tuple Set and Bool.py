# Tuples
# Similar to List
# But it is immutable i.e. Its values cannot be modified once created

# Defining a Tuple
mytup = tuple()
mytup = ()

# Tuple with data
mytup = (1,2,3,4,4,3,3,4,3)
print(mytup)

# Length of Tuple
print(len(mytup))

# Accessing Values
print(mytup[0])
print(mytup[1])

# Count
print(mytup.count(3))

# Find Index
print(mytup.index(1))
print(mytup.index(3))

# Its value cannot be changed
# This will result in error
# mytup[0] = 10


# Sets
# Unordered Collection of Unique Elements
# Also represented by {} but not in key value pairs

# Defining Sets
myset = set()
myset = {1,2,3,4}

# Adding Element to set
myset.add(5)
print(myset)

myset.add(5)
print(myset)

# Operation on sets
myset2 = {3,4,5,6}

# Union
print(myset.union(myset2))

# Intersection
print(myset.intersection(myset2))

# Difference
print(myset.difference(myset2))

# Symmetric Difference
print(myset.symmetric_difference(myset2))



# Booleans
# Only has 2 values - True or False
# Used in Control Flow
mybool = True
print(mybool)
mybool = False
print(mybool)