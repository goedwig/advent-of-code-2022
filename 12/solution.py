from collections import deque

ROW_COUNT = 41
COL_COUNT = 179

X_DELTA = [-1, 0, 0, 1]
Y_DELTA = [0, -1, 1, 0]


class Cell:
    def __init__(self, x: int, y: int, value: str) -> None:
        self.x = x
        self.y = y
        self.value = value

    def __eq__(self, other: "Cell") -> bool:
        return self.x == other.x and self.y == other.y


class QueueNode:
    def __init__(self, cell: Cell, distance: int) -> None:
        self.cell = cell
        self.distance = distance


def coords_valid(x: int, y: int) -> bool:
    return (0 <= x < ROW_COUNT) and (0 <= y < COL_COUNT)


def movement_possible(source: Cell, dest: Cell) -> bool:
    return ord(dest.value) - ord(source.value) <= 1


def bfs_lee(matrix: list[list[str]], source: Cell, dest: Cell) -> int | None:
    visited = [[False for _ in range(COL_COUNT)] for _ in range(ROW_COUNT)]

    visited[source.x][source.y] = True

    q = deque()

    q.append(QueueNode(source, 0))

    while q:
        current_node = q.popleft()
        current_cell = current_node.cell

        if current_cell == dest:
            return current_node.distance

        for i in range(4):
            x_next = current_cell.x + X_DELTA[i]
            y_next = current_cell.y + Y_DELTA[i]

            if coords_valid(x_next, y_next) and not visited[x_next][y_next]:
                next_cell = Cell(x_next, y_next, matrix[x_next][y_next])

                if movement_possible(current_cell, next_cell):
                    visited[x_next][y_next] = True
                    q.append(QueueNode(next_cell, current_node.distance + 1))

    return None


with open("12/input.txt") as f:
    heightmap = [list(line) for line in f.read().replace("S", "a").replace("E", "z").splitlines()]


def part_1():
    source_x, source_y = 20, 0
    source = Cell(source_x, source_y, heightmap[source_x][source_y])

    dest_x, dest_y = 20, 154
    dest = Cell(dest_x, dest_y, heightmap[dest_x][dest_y])

    distance = bfs_lee(matrix=heightmap, source=source, dest=dest)

    print(f"Shortest distance from 'S' to 'E': {distance}")


def part_2():
    min_distance = None

    dest_x, dest_y = 20, 154
    dest = Cell(dest_x, dest_y, heightmap[dest_x][dest_y])

    for x in range(ROW_COUNT):
        for y in range(COL_COUNT):
            if heightmap[x][y] != "a":
                continue
            source = Cell(x, y, heightmap[x][y])
            distance = bfs_lee(matrix=heightmap, source=source, dest=dest)
            if distance:
                min_distance = distance if min_distance is None else min(min_distance, distance)

    print(f"Shortest distance from any 'a' to 'E': {min_distance}")


part_1()
part_2()
