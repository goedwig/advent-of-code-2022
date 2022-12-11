max_elf_calories = 0
elf_calories = 0

f = open("01/input.txt")

for line in f:
    line = line.rstrip()
    if not line:
        max_elf_calories = max(max_elf_calories, elf_calories)
        elf_calories = 0
        continue
    elf_calories += int(line)

print(max_elf_calories)
