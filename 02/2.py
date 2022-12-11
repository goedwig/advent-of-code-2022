score_map = {
    "B X": 1,
    "C X": 2,
    "A X": 3,
    "A Y": 4,
    "B Y": 5,
    "C Y": 6,
    "C Z": 7,
    "A Z": 8,
    "B Z": 9,

}
score = 0

f = open("2/input.txt")

for line in f:
    score += score_map[line.rstrip()]

print(score)
