from scan_cave import scan_cave, WIDTH, HEIGHT

SAND_X, SAND_Y = 500, 0


def solution():
    rest_count = 0
    while True:
        x, y = SAND_X, SAND_Y
        while True:
            if x <= 0 or x >= WIDTH - 1 or y >= HEIGHT - 1:
                return rest_count

            if cave[y + 1][x] == ".":  # air, go down
                y += 1
            elif cave[y + 1][x - 1] == ".":  # diagonal left
                y += 1
                x -= 1
            elif cave[y + 1][x + 1] == ".":  # diagonal right
                y += 1
                x += 1
            else:  # sand comes to rest
                cave[y][x] = "o"
                rest_count += 1
                if x == SAND_X and y == SAND_Y:  # cave with floor
                    return rest_count
                else:
                    break


# part 1
cave = scan_cave()
print(solution())
with open("14/solution_cave.txt", "w") as f:
    f.write("\n".join("".join(row) for row in cave))

# part 2
cave = scan_cave(floor=True)
print(solution())
with open("14/solution_cave_with_floor.txt", "w") as f:
    f.write("\n".join("".join(row) for row in cave))
