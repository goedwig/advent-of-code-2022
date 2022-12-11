from functools import reduce
from string import ascii_letters

priorities_sum = 0

with open("03/input.txt") as f:
    lines = [line.rstrip() for line in f.readlines()]


for i in range(0, len(lines), 3):
    group = lines[i:(i + 3)]
    badge = reduce(set.intersection, map(set, group)).pop()
    priorities_sum += ascii_letters.index(badge) + 1

print(priorities_sum)
