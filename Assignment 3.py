# Even or Odd Checker Write a Python program that takes an integer input from the user and determines whether the number is even or odd using an if-else stat# Find the Largest Number Create a Python program that takes three numbers as input and uses if-else conditions to find and display the largest number.
num1 = int(input("Even or Odd: "))
if num1 % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")


# Find the Largest Number Create a Python program that takes three numbers as input and uses if-else conditions to find and display the largest number.
a, b, c = map(int, input("Enter three unique numbers separated by a space: ").split())
if a > b and a > c:
    print("a is big")
elif b > c:
    print("b is big")
else:
    print("c is big")

# Number Classification Write a program that takes a number input and checks if the number is positive, negative, or zero using if-elif-else conditions.
num2 = int(input("Positive or Negative: "))
if num2 > 0:
    print("Given number is positive")
elif num2 < 0:
    print("Given number is negative")
else:
    print("Given number is zero")

# Sum of Numbers in a Range Write a Python program that takes two numbers (start and end) as input and uses a for loop to compute and display the sum of all numbers in that range.
sum = 0
start = int(input("Start of the loop: "))
end = int(input("End of the loop: "))
for i in range(start, end+1):
    sum += i
    print(sum)


# Printing a Multiplication Table Develop a Python program that takes an integer as input and prints its multiplication table from 1 to 10 using a for loop.
num3 = int(input("Table "))
for i in range(1, 11):
    print(f"{num3} x {i} = {num3*i}")


# Counting Vowels in a String Write a Python script that takes a string input from the user and uses a for loop to count the number of vowels (a, e, i, o, u) present in the string.
vowel_count = 0
vowels = "aeiou"
str1 = input("To check the vowel count: ")
for i in str1:
    if i in vowels:
        vowel_count += 1
print(vowel_count)


num4 = int(input("Factorial of :"))
factorial = 1
for i in range(1, num4+1):
    factorial *= i
print(factorial)


# FizzBuzz Game Write a Python program that prints numbers from 1 to 50. However:

# For multiples of 3, print "Fizz" instead of the number.

# For multiples of 5, print "Buzz".

# For numbers that are multiples of both 3 and 5, print "FizzBuzz".
for i in range(1, 51):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")


for i in range(1, 6):
    for j in range(i):
        print("*", end=' ')
    print()
