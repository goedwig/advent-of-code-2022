from functools import reduce

with open("08/input.txt") as f:
    tree_map = [list(map(int, line)) for line in f.read().splitlines()]

best_scenic_score = 0

for i in range(len(tree_map)):
    for j in range(len(tree_map[i])):
        tree_height = tree_map[i][j]
        viewing_distances = [0, 0, 0, 0]

        for k in range(i - 1, -1, -1):
            viewing_distances[0] += 1
            if tree_map[k][j] >= tree_height:
                break

        for k in range(i + 1, len(tree_map), 1):
            viewing_distances[1] += 1
            if tree_map[k][j] >= tree_height:
                break

        for k in range(j - 1, -1, -1):
            viewing_distances[2] += 1
            if tree_map[i][k] >= tree_height:
                break

        for k in range(j + 1, len(tree_map[i]), 1):
            viewing_distances[3] += 1
            if tree_map[i][k] >= tree_height:
                break

        best_scenic_score = max(best_scenic_score, reduce(lambda a, b: a * b, viewing_distances))

print(best_scenic_score)
