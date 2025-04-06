# Assign the string "Hello, World!" to a variable and print it.
n = "Hello, World!"
print(n)

# Create a string "Python Programming" and extract the first five characters using slicing.
n = "Python Programming"
print(n[:5])

# Given a string "python is fun", convert it to uppercase.
n = "python is fun"
print(n.upper())

# Replace "fun" with "awesome" in the string "Python is fun".
n.replace("fun", "awesome")

# Use f-string formatting to create a message like "My name is John, and I am 25 years old.", where the name and age are variables.
name = "John"
age = 25
print(f"My name is {name}, and I am {age} years old.")

# Given a price of 49.99, format it to display only two decimal places.
price = 49.99
print("{:.2f}".format(price))

# Count the occurrences of the letter 'o' in "Hello, how are you?".
n = "Hello, How are you?"
print(n.count('o'))

# Find the position of "world" in "Hello, world! Python is amazing.".
n = "Hello, World! Python is amazing"
print(n.index("World"))

# Reverse the string "Python" using slicing.
n = "Python"
print(n[::-1])

# Check if "madam" is a palindrome (a word that reads the same forward and backward).
n = "madam"
if n == n[::-1]:
    print(f"{n} is a Palindrome")
else:
    print(f"{str7} is not a Palindrome")
