

list1 = [1, 4, 2, 4, 9]
list2 = [1, 16, 4, 16, 16]

for number in list1:
    if not number**2 in list2:
        print("false")
