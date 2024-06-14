
# create a list with x repeated y times

import random
count = [0] * 26
nonesuch = [None] * 10


# make a list (array) of things a key in a dict

collection = {}
randoms = [random.randint(1, 10) for _ in range(10)]
key = tuple(randoms)

collection[key] = ["random pattern 1"]

# sorting a string

s = "Zunnikins"
change_case = "".join(sorted(s.lower()))
preserve_case = "".join(sorted(s, key=lambda c: (c.lower(), c)))
