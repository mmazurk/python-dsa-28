# Exercise 1: Simple Arithmetic Operations
# Create lambda functions to perform basic arithmetic operations.
from functools import reduce
def add(x, y): return x + y
def subtract(x, y): return x - y
def multiply(x, y): return x * y
def divide(x, y): return x / y


# Test the arithmetic lambda functions
print("Addition (3 + 5):", add(3, 5))         # Output: 8
print("Subtraction (10 - 4):", subtract(10, 4))  # Output: 6
print("Multiplication (2 * 7):", multiply(2, 7))  # Output: 14
print("Division (20 / 4):", divide(20, 4))       # Output: 5.0

# Exercise 2: List Sorting
# Sort a list of tuples based on the second element of each tuple.
sorted_list = sorted([(1, 2), (3, 1), (5, 4), (2, 3)], key=lambda x: x[1])
print("Sorted list by second element:", sorted_list)
# Output: [(3, 1), (1, 2), (2, 3), (5, 4)]

# Exercise 3: Filtering Lists
# Filter a list of numbers, keeping only the even numbers.
even_numbers = list(filter(lambda x: x %
                    2 == 0, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print("Even numbers:", even_numbers)
# Output: [2, 4, 6, 8, 10]

# Exercise 4: Mapping Function
# Square each number in a list.
squares = list(map(lambda x: x ** 2, [1, 2, 3, 4, 5]))
print("Squares of numbers:", squares)
# Output: [1, 4, 9, 16, 25]

# Exercise 5: Reducing Lists
# Find the product of all numbers in a list.
product = reduce(lambda x, y: x * y, [1, 2, 3, 4, 5])
print("Product of all numbers:", product)
# Output: 120

# Exercise 6: Conditional Lambda
# Return "Even" if a number is even and "Odd" if a number is odd.


def even_odd(x): return "Even" if x % 2 == 0 else "Odd"


print("10 is:", even_odd(10))  # Output: "Even"
print("15 is:", even_odd(15))  # Output: "Odd"

# Exercise 7: Combining Lambdas
# Calculate the average of three numbers.


def average(x, y, z): return (x + y + z) / 3


print("Average of 10, 20, 30:", average(10, 20, 30))  # Output: 20.0

# Exercise 8: String Manipulation
# Convert a list of strings to uppercase.
uppercase = list(map(lambda s: s.upper(), ["hello", "world", "python"]))
print("Uppercase strings:", uppercase)
# Output: ['HELLO', 'WORLD', 'PYTHON']

# Exercise 9: Dictionary with Lambdas
# Create a dictionary where the values are lambda functions that compute the square of the key.
lambda_dict = {x: (lambda x=x: x**2) for x in range(1, 6)}
print("Square of 5 using lambda in dictionary:",
      lambda_dict[5]())  # Output: 25

# Exercise 10: Lambda for Custom Sorting
# Sort a list of strings based on their length.
sorted_by_length = sorted(
    ["apple", "banana", "cherry", "date"], key=lambda x: len(x))
print("Sorted list by string length:", sorted_by_length)
# Output: ['date', 'apple', 'banana', 'cherry']
