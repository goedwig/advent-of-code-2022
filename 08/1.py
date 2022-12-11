with open("08/input.txt") as f:
    tree_map = [list(map(int, line)) for line in f.read().splitlines()]

visible = len(tree_map) * 4 - 4

for i in range(1, len(tree_map) - 1):
    for j in range(1, len(tree_map[i]) - 1):
        tree_height = tree_map[i][j]
        is_visible = False

        for k in range(i - 1, -1, -1):
            if tree_height <= tree_map[k][j]:
                break
        else:
            is_visible = True

        for k in range(i + 1, len(tree_map), 1):
            if tree_height <= tree_map[k][j]:
                break
        else:
            is_visible = True

        for k in range(j - 1, -1, -1):
            if tree_height <= tree_map[i][k]:
                break
        else:
            is_visible = True

        for k in range(j + 1, len(tree_map[i]), 1):
            if tree_height <= tree_map[i][k]:
                break
        else:
            is_visible = True

        visible += is_visible

print(visible)
