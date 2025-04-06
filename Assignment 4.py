# Create a tuple named my_tuple containing at least five different elements (mix of integers, strings, and a float).
my_tuple = (1, 2, "Sai", "Mohan", 55.5)

# Print the tuple.
print(my_tuple)

# Accessing Elements
print(*my_tuple)
for i in my_tuple:
    print(i)

# Print the first and last element of my_tuple using indexing.
print(my_tuple[0])
print(my_tuple[-1])

# Use negative indexing to access the second last element.
print(my_tuple[-2])

# Tuple Slicing
print(my_tuple[2:4])

# Slice and print the first three elements of my_tuple.
print(my_tuple[:3])

# Slice and print the last two elements.
print(my_tuple[: -3: -1])

# Tuple Operations
my_tup = (1, 2, 3, 4, 5)
print(len(my_tup))
print(max(my_tup))
print(min(my_tup))
print(sum(my_tup))

# Concatenate my_tuple with another tuple and print the result.
print(my_tuple+my_tup)

# Repeat my_tuple twice and print the result.
print(my_tuple*2)

# Tuple Methods
print(my_tuple.index("Sai"))
print(my_tuple.count(2))

# Find the index of a specific element in my_tuple and print it.
print(my_tuple.index(1))

# Count the occurrences of a specific element in my_tuple and print it.
print(my_tuple.count("Mohan"))

# Try changing one element in my_tuple and observe
# my_tuple[2] = 6 I tried this and it returned an error.
"""The error is 
TypeError: 'tuple' object does not support item assignment
"""
# Explain why tuples are immutable.
"""_summary_
Tuples are immutable meaning they cannot be changed.Precisely speaking, we cannot change their values, their size.
We cannot append, insert, remove, pop, and some other mutable methods. The only thing we can perform on tuples is  index and count
which can only retrive information but won't change anything.
"""
# Tuple Packing and Unpacking
packing_tuple = 1, 2, 3
print(packing_tuple)

# Create a tuple with three elements and unpack them into individual variables.
a, b, c = packing_tuple

# Print the unpacked values.
print(a)
print(b)
print(c)

# Use a loop to iterate through my_tuple and print each element.
for i in my_tuple:
    print(i)

# Write a function that returns multiple values using a tuple.
def tuplefunc(tup):
    a, b, c, d, e = my_tuple
    return a, b, c, d, e

# Call the function and print the returned tuple.
print(tuplefunc(my_tuple))
