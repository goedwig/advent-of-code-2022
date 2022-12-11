from collections import defaultdict
from functools import reduce
from operator import itemgetter

from input import monkeys


def solve(monkeys, rounds, decrease):
    inspected_count_by_monkey = defaultdict(int)

    for _ in range(rounds):
        for idx, monkey in enumerate(monkeys):
            while monkey["items"]:
                old = monkey["items"].pop(0)
                new = decrease(monkey["operation"](old))
                if new % monkey["divider"] == 0:
                    monkeys[monkey["next_true"]]["items"].append(new)
                else:
                    monkeys[monkey["next_false"]]["items"].append(new)
                inspected_count_by_monkey[idx] += 1

    max_1, max_2 = sorted(inspected_count_by_monkey.values(), reverse=True)[:2]
    print(max_1 * max_2)


# Part 1
solve(monkeys[:], 20, lambda value: value // 3)

# Part 2 🍑🔥
divider_product = reduce(lambda a, b: a * b, map(itemgetter("divider"), monkeys))
solve(monkeys[:], 10_000, lambda value: value % divider_product)
