# Exercise 1: Simple Arithmetic Operations
# Create lambda functions to perform basic arithmetic operations.

from functools import reduce
def add(x, y): return x + y
def sub(x, y): return x - y
def mult(x, y): return x * y
def div(x, y): return x / y


# Exercise 2: List Sorting
# Sort a list of tuples based on the second element of each tuple.
# Output: [(3, 1), (1, 2), (2, 3), (5, 4)]
tuples = [(3, 1), (1, 2), (2, 3), (5, 4)]
sorted_tuples = sorted(tuples, key=lambda x: x[0])
sorted_tuples

# Exercise 3: Filtering Lists
# Filter a list of numbers, keeping only the even numbers.
# Output: [2, 4, 6, 8, 10]
my_nums = list(range(1, 6))
even_numbers = list(filter(lambda x: x % 2 == 0, my_nums))
even_numbers

# Exercise 4: Mapping Function
# Square each number in a list.
# Output: [1, 4, 9, 16, 25]
squares = list(map(lambda x: x**2, my_nums))

# Exercise 5: Reducing Lists
# Find the product of all numbers in a list.
# Output: 120
product = reduce(lambda x, y: x * y, my_nums)

# Exercise 6: Conditional Lambda
# Return "Even" if a number is even and "Odd" if a number is odd.
evens_odds = list(map(lambda x: "even" if x % 2 == 0 else "odd", my_nums))

# Exercise 7: Combining Lambdas
# Calculate the average of three numbers.


def average_three(x, y, z): return (x + y + z)/3


average_three(100, 100, 99)

# Exercise 8: String Manipulation
# Convert a list of strings to uppercase.
# Output: ['HELLO', 'WORLD', 'PYTHON']
words = ["hello", "world", "python"]
uppercase_words = list(map(lambda x: x.upper(), words))

# Exercise 9: Dictionary with Lambdas
# Create a dictionary where the values are lambda functions that compute the square of the key.

# Exercise 10: Lambda for Custom Sorting
# Sort a list of strings based on their length.
# Output: ['date', 'apple', 'banana', 'cherry']
