score_map = {
    "B X": 1,
    "C Y": 2,
    "A Z": 3,
    "A X": 4,
    "B Y": 5,
    "C Z": 6,
    "C X": 7,
    "A Y": 8,
    "B Z": 9,
}
score = 0

f = open("02/input.txt")

for line in f:
    score += score_map[line.rstrip()]

print(score)
