# Given list of tuples
coordinates = [(1, 2), (3, 4), (5, 6)]

# Loop to unpack and print each coordinate
for x, y in coordinates:
    print(f"Coordinate: ({x}, {y})")
# Expected Output:
# Coordinate: (1, 2)
# Coordinate: (3, 4)
# Coordinate: (5, 6)

# Given dictionary of student grades
student_grades = {"Alice": 85, "Bob": 92, "Charlie": 78}

# Loop to iterate through the dictionary and print each student's name and grade
for student, grade in student_grades.items():
    print(f"{student}: {grade}")
# Expected Output:
# Alice: 85
# Bob: 92
# Charlie: 78

# Given list of lists
nested_lists = [["apple", "red", 1.2], [
    "banana", "yellow", 0.5], ["cherry", "red", 0.2]]

# Loop to unpack and print each sublist's elements
for fruit, color, weight in nested_lists:
    print(f"The {fruit} is {color} and weighs {weight}kg")
# Expected Output:
# The apple is red and weighs 1.2kg
# The banana is yellow and weighs 0.5kg
# The cherry is red and weighs 0.2kg

# Given list of strings
fruits = ["apple", "banana", "cherry"]

# Loop to print each string with its index
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")
# Expected Output:
# 0: apple
# 1: banana
# 2: cherry

# Given lists
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]

# Loop to iterate over both lists and print each name with its corresponding age
for name, age in zip(names, ages):
    print(f"{name} is {age} years old")
# Expected Output:
# Alice is 25 years old
# Bob is 30 years old
# Charlie is 35 years old

# Given list of dictionaries
people = [{"name": "Alice", "age": 25}, {
    "name": "Bob", "age": 30}, {"name": "Charlie", "age": 35}]

# Loop to iterate and unpack each dictionary
for person in people:
    name = person["name"]
    age = person["age"]
    print(f"{name} is {age} years old")
# Expected Output:
# Alice is 25 years old
# Bob is 30 years old
# Charlie is 35 years old

# Loop to iterate over a range with steps
for number in range(0, 21, 5):
    print(number)
# Expected Output:
# 0
# 5
# 10
# 15
# 20

# Given list of numbers
numbers = [1, 2, 3, 4, 5]

# List to hold squared numbers
squared_numbers = []

# Loop to square each number and add to the new list
for number in numbers:
    squared_numbers.append(number ** 2)

print("Squared numbers:", squared_numbers)
# Expected Output:
# Squared numbers: [1, 4, 9, 16, 25]

# Given list of tuples
people_info = [("Alice", 25, "New York"), ("Bob", 30,
                                           "San Francisco"), ("Charlie", 35, "Chicago")]

# Loop to unpack and print each person's information
for name, age, city in people_info:
    print(f"{name} is {age} years old and lives in {city}")
# Expected Output:
# Alice is 25 years old and lives in New York
# Bob is 30 years old and lives in San Francisco
# Charlie is 35 years old and lives in Chicago

# Given list of fruits
fruits = ["apple", "banana", "cherry"]

# Loop to iterate over indexes and print each fruit with its index
for i in range(len(fruits)):
    print(f"{i}: {fruits[i]}")
# Expected Output:
# 0: apple
# 1: banana
# 2: cherry
