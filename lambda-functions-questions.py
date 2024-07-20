# Exercise 1: Simple Arithmetic Operations
# Create lambda functions to perform basic arithmetic operations.

def add(x, y): return x + y
def subtract(x, y): return x - y
def multiply(x, y): return x * y
def divide(x, y): return x / y


# Exercise 2: List Sorting
# Sort a list of tuples based on the second element of each tuple.
# Output: [(3, 1), (1, 2), (2, 3), (5, 4)]
tuples = [(3, 1), (1, 2), (2, 3), (5, 4)]
sorted_tuples = sorted(tuples, key=lambda x: x[0])
sorted_tuples

# Exercise 3: Filtering Lists
# Filter a list of numbers, keeping only the even numbers.
# Output: [2, 4, 6, 8, 10]
nums_list = list(range(11))
new_list = list(filter(lambda x: x % 2 == 0), nums_list)
new_list

# Exercise 4: Mapping Function
# Square each number in a list.
# Output: [1, 4, 9, 16, 25]

# Exercise 5: Reducing Lists
# Find the product of all numbers in a list.
# Output: 120

# Exercise 6: Conditional Lambda
# Return "Even" if a number is even and "Odd" if a number is odd.

# Exercise 7: Combining Lambdas
# Calculate the average of three numbers.

# Exercise 8: String Manipulation
# Convert a list of strings to uppercase.
# Output: ['HELLO', 'WORLD', 'PYTHON']


# Exercise 9: Dictionary with Lambdas
# Create a dictionary where the values are lambda functions that compute the square of the key.

# Exercise 10: Lambda for Custom Sorting
# Sort a list of strings based on their length.
# Output: ['date', 'apple', 'banana', 'cherry']
