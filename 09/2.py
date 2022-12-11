with open("09/input.txt") as f:
    moves = [(line[0], int(line[2:])) for line in f.read().splitlines()]

Hx, Hy = 0, 0
Tx = [0] * 9
Ty = [0] * 9

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

        hx, hy = Hx, Hy
        for k in range(9):
            tx, ty = Tx[k], Ty[k]

            if abs(hx - tx) <= 1 and abs(hy - ty) <= 1:
                break

            if hx == tx or hy == ty:
                deltas = ((0, 1), (0, -1), (1, 0), (-1, 0))
            else:
                deltas = ((1, 1), (1, -1), (-1, 1), (-1, -1))

            for dx, dy in deltas:
                tx_new, ty_new = tx + dx, ty + dy
                if abs(hx - tx_new) <= 1 and abs(hy - ty_new) <= 1:
                    Tx[k], Ty[k] = tx_new, ty_new

            hx, hy = Tx[k], Ty[k]

        T_visited.add((Tx[-1], Ty[-1]))

print(len(T_visited))
