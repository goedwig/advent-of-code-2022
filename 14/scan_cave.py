WIDTH = 1000
HEIGHT = 200


def scan_cave(floor=False):
    paths = []
    with open("14/input.txt") as f:
        while line := f.readline():
            path = [tuple(map(int, point.split(","))) for point in line.split(" -> ")]
            paths.append(path)

    cave = [["."] * WIDTH for _ in range(HEIGHT)]
    max_y = 0

    for path in paths:
        for i in range(len(path) - 1):
            (x0, y0), (x1, y1) = path[i], path[i + 1]
            max_y = max(max_y, y0, y1)
            x_d = (x0 < x1) - (x0 > x1)
            y_d = (y0 < y1) - (y0 > y1)
            while True:
                cave[y0][x0] = "#"
                if x0 == x1 and y0 == y1:
                    break
                x0 += x_d
                y0 += y_d

    if floor:
        cave[max_y + 2] = ["#"] * WIDTH

    return cave


if __name__ == "__main__":
    cave = scan_cave()
    with open("14/cave.txt", "w") as f:
        f.write("\n".join("".join(row) for row in cave))
