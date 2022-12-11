with open("09/input.txt") as f:
    moves = [(line[0], int(line[2:])) for line in f.read().splitlines()]

Hx, Hy = 0, 0
Tx, Ty = 0, 0

T_visited = {(0, 0)}


def inc(x, y, direction):
    match direction:
        case "U":
            return x, y + 1
        case "D":
            return x, y - 1
        case "L":
            return x - 1, y
        case "R":
            return x + 1, y

for direction, count in moves:
    for _ in range(count):
        Hx, Hy = inc(Hx, Hy, direction)

        if abs(Hx - Tx) <= 1 and abs(Hy - Ty) <= 1:
            continue

        if Hx == Tx or Hy == Ty:
            deltas = ((0, 1), (0, -1), (0, 1), (0, -1), (1, 0), (-1, 0))
        else:
            deltas = ((1, 1), (1, -1), (-1, 1), (-1, -1))

        for dx, dy in deltas:
            Tx_new, Ty_new = Tx + dx, Ty + dy
            if abs(Hx - Tx_new) <= 1 and abs(Hy - Ty_new) <= 1:
                Tx = Tx_new
                Ty = Ty_new
                T_visited.add((Tx, Ty))
                break

print(len(T_visited))
