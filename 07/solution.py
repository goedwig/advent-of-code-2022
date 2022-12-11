class Dir:
    def __init__(self):
        self.size = 0
        self.parent = None
        self.children = []


root_dir = Dir()
current_dir = root_dir

with open("07/input.txt") as f:
    f.readline()  # skip first '$ cd /'
    terminal_output = [line.rstrip().removeprefix("$ ") for line in f]

for line in terminal_output:
    if line.startswith("cd"):
        directory = line.split(" ")[1]
        if directory == "..":
            current_dir = current_dir.parent
        else:
            child_dir = Dir()
            child_dir.parent = current_dir
            current_dir.children.append(child_dir)
            current_dir = child_dir
    elif line[0].isdigit():
        size = int(line.split(" ")[0])
        current_dir.size += size
        d = current_dir
        while d.parent is not None:
            d = d.parent
            d.size += size


# Part 01

def calc_sum(current_dir):
    result_sum = 0

    for child_dir in current_dir.children:
        result_sum += calc_sum(child_dir)

    if current_dir.size <= 100_000:
        result_sum += current_dir.size

    return result_sum


print(calc_sum(root_dir))

# Part 02

total_space = 70_000_000
free_space = total_space - root_dir.size

final_space = 30_000_000
space_to_free = final_space - free_space


def find_dir_to_delete(current_dir, current_smallest):
    for child_dir in current_dir.children:
        current_smallest = find_dir_to_delete(child_dir, current_smallest)

    if current_dir.size >= space_to_free:
        return min(current_smallest, current_dir.size)
    else:
        return current_smallest


print(find_dir_to_delete(root_dir, root_dir.size))
