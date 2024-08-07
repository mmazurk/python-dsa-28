
# using range()


# create a list with x repeated y times

from random import randint
count = [0] * 26
nonesuch = [None] * 10

# make a list (array) of things a key in a dict

collection = {}
randoms = [randint(1, 10) for _ in range(10)]
key = tuple(randoms)

collection[key] = ["random pattern 1"]

# sorting a string

s = "Zunnikins"
change_case = "".join(sorted(s.lower()))
preserve_case = "".join(sorted(s, key=lambda c: (c.lower(), c)))

# don't ever generate dynamic variable names
# use a list or dict to store things


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"{self.val} --> {self.next}"


items = [1, 2, 3, 4, 5]
listnodes = []
for item in items:
    listnodes.append(ListNode(item))


results = {}
for i in range(5):
    results[f"value_{i}"] = (i)*12


# Study this pattern because it really gets you
# Set the conditions (previous, current)
# Iterate and do logic you need to do (e.g., flip the arrow)
# Then within the loop, set the conditions again

head = ListNode(1)

previous_node = None
current_node = head

while (current_node):
    next_node = current_node.next
    current_node.next = previous_node
    previous_node = current_node
    current_node = next_node


# This is a basic pattern you need to learn for recursion

def reverse_list_recursive(lst):

    if len(lst) <= 1:
        return lst

    reversed = reverse_list_recursive(lst[1:])
    reversed.append(lst[0])

    return reversed


reverse_list_recursive([1, 2, 3, 4, 5])
