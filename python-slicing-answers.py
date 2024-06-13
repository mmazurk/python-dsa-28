# Exercise 1
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# 1. First 5 elements
print(numbers[:5])

# 2. Last 3 elements
print(numbers[-3:])

# 3. Elements from index 3 to 7
print(numbers[3:8])

# 4. Every second element
print(numbers[::2])

# 5. Every second element starting from index 1
print(numbers[1::2])

# Exercise 2
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

# 1. Last 4 elements
print(letters[-4:])

# 2. First 4 elements using negative indices
print(letters[:-4])

# 3. All elements except the last one
print(letters[:-1])

# 4. All elements in reverse order
print(letters[::-1])

# 5. Every second element in reverse order
print(letters[::-2])

# Exercise 3
sequence = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# 1. Every third element
print(sequence[::3])

# 2. Elements from index 2 to the end with a step of 2
print(sequence[2::2])

# 3. Elements from index 5 to index 1 in reverse order
print(sequence[5:0:-1])

# 4. Elements from index 6 to the start in reverse order
print(sequence[6::-1])

# 5. Every fourth element from end to start
print(sequence[::-4])

# Exercise 4
mix = ['a', 1, 'b', 2, 'c', 3, 'd', 4, 'e', 5]

# 1. Elements at even indices
print(mix[::2])

# 2. Elements at odd indices
print(mix[1::2])

# 3. First three pairs of elements
print([mix[i:i+2] for i in range(0, 6, 2)])

# 4. Reverse list except first and last elements
print(mix[-2:0:-1])

# 5. Pairs in reverse order
print([mix[i:i+2] for i in range(8, -1, -2)])

# Exercise 5
text = "PythonSlicing"

# 1. First 6 characters
print(text[:6])

# 2. Last 7 characters
print(text[-7:])

# 3. Characters from index 3 to 8
print(text[3:9])

# 4. Every second character
print(text[::2])

# 5. Reverse the entire string
print(text[::-1])
