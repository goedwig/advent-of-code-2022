with open("10/input.txt") as f:
    instructions = []
    for instr in f.read().splitlines():
        if instr.startswith("addx"):
            instructions.append("noop")
        instructions.append(instr)

# Part 01

X = 1
X_sum = 0

for cycle, instr in enumerate(instructions, start=1):
    if cycle in (20, 60, 100, 140, 180, 220):
        X_sum += X * cycle

    if instr.startswith("addx"):
        X += int(instr[5:])

print(X_sum)

# Part 02

CRT = [["."] * 40 for _ in range(6)]
cycle = 0
X = 1

for row in CRT:
    for i in range(40):
        instr = instructions[cycle]

        if i in range(X - 1, X + 2):
            row[i] = "#"

        if instr.startswith("addx"):
            X += int(instr[5:])

        cycle += 1

print("\n".join("".join(row) for row in CRT))
