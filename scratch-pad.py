

mark = list(range(0, 10))
print(mark)


for i in range(1, 10):
    print(f"Iteration #", i)
    for j in range(10, 0, -1):
        print(f"Inner Loop Number", j)
