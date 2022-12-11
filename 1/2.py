top_three = [0, 0, 0]
elf_calories = 0

f = open("1/input.txt")

for line in f:
    line = line.rstrip()

    if line:
        elf_calories += int(line)
        continue

    for i in range(3):
        if elf_calories > top_three[i]:
            top_three.insert(i, elf_calories)
            top_three.pop()
            break

    elf_calories = 0

print(top_three)
print(sum(top_three))
