from string import ascii_letters

priorities_sum = 0

f = open("3/input.txt")

for line in f:
    line = line.rstrip()
    half = len(line) // 2

    left, right = line[:half], line[half:]

    common = set(left) & set(right)

    for item in common:
        priorities_sum += ascii_letters.index(item) + 1

print(priorities_sum)
