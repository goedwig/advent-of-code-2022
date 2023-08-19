import copy
import json


def preprocess(left, right):
    min_len = min(len(left), len(right))
    for i in range(min_len):
        if type(left[i]) == type(right[i]) == int:
            continue
        if isinstance(left[i], int):
            left[i] = [left[i]]
        elif isinstance(right[i], int):
            right[i] = [right[i]]
        preprocess(left[i], right[i])


def part_1():
    indices_sum = 0
    index = 1

    with open("13/input.txt") as f:
        while True:
            left = json.loads(f.readline())
            right = json.loads(f.readline())

            preprocess(left, right)

            if left < right:
                indices_sum += index

            index += 1

            if not f.readline():
                break

    print(indices_sum)


def part_2():
    packets = []
    with open("13/input.txt") as f:
        while True:
            packets += [
                json.loads(f.readline()),
                json.loads(f.readline()),
            ]
            if not f.readline():
                break

    packets += [
        [[2]],
        [[6]],
    ]

    for i in range(len(packets) - 1):
        for j in range(i + 1, len(packets)):
            left = copy.deepcopy(packets[i])
            right = copy.deepcopy(packets[j])

            preprocess(left, right)

            if right < left:
                packets[i], packets[j] = packets[j], packets[i]

    print((packets.index([[2]]) + 1) * (packets.index([[6]]) + 1))

part_2()
