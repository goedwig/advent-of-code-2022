f = open("04/input.txt")

overlap = 0

for line in f:
    line = line.rstrip()
    bounds_1, bounds_2 = line.split(",")
    bounds_1 = tuple(map(int, bounds_1.split("-")))
    bounds_2 = tuple(map(int, bounds_2.split("-")))

    range_1 = range(bounds_1[0], bounds_1[1] + 1)
    range_2 = range(bounds_2[0], bounds_2[1] + 1)

    if set(range_1) & set(range_2):
        overlap += 1

print(overlap)
