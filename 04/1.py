f = open("04/input.txt")

full_containment = 0

for line in f:
    line = line.rstrip()
    bounds_1, bounds_2 = line.split(",")
    bounds_1 = tuple(map(int, bounds_1.split("-")))
    bounds_2 = tuple(map(int, bounds_2.split("-")))

    if bounds_1[0] >= bounds_2[0] and bounds_1[1] <= bounds_2[1]:
        full_containment += 1
    elif bounds_2[0] >= bounds_1[0] and bounds_2[1] <= bounds_1[1]:
        full_containment += 1

print(full_containment)
