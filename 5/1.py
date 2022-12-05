from operator import itemgetter

with open("5/input.txt") as f:
    lines = [line.rstrip() for line in f.readlines()]

drawing, instructions = lines[7::-1], lines[10:]

stacks = [[] for _ in range(9)]

for line in drawing:
    for stack_idx, crate_idx in enumerate(range(1, len(line) - 1, 4)):
        if (crate := line[crate_idx]) != " ":
            stacks[stack_idx].append(crate)

for instruction in instructions:
    count, src, dest = map(int, itemgetter(1, 3, 5)(instruction.split(" ")))
    for _ in range(count):
        stacks[dest - 1].append(stacks[src - 1].pop())

message = "".join(stack.pop() for stack in stacks)

print(message)
