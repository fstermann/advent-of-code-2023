import os
from collections import defaultdict

import pytest

from aoc.utils import read_input

INPUT_TXT = os.path.join(os.path.dirname(__file__), "input.txt")


def run(input_: str) -> int:
    all_copies = defaultdict(int)

    for line in input_.splitlines():
        idx, cards = line.split(": ")
        idx = int(idx.replace("Card ", ""))
        winning, mine = cards.split(" | ")
        winning = {int(i) for i in winning.split()}
        mine = {int(i) for i in mine.split()}

        if n := len(winning & mine):
            card_copies = all_copies[idx] + 1
            all_copies.update({c: all_copies[c] + card_copies for c in range(idx + 1, idx + n + 1)})
        all_copies[idx] += 1
    return sum(all_copies.values())


INPUT = """\
Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
"""
EXPECTED = 30


@pytest.mark.parametrize(("input_", "expected"), ((INPUT, EXPECTED),))
def test_puzzle(input_, expected):
    assert run(input_) == expected


if __name__ == "__main__":
    input_ = read_input(INPUT_TXT)
    print(run(input_))
