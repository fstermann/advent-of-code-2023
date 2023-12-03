import functools
import operator
import os
from dataclasses import dataclass, field

import pytest

from aoc.utils import read_input

INPUT_TXT = os.path.join(os.path.dirname(__file__), "input.txt")


@dataclass
class Number:
    num: int
    neighbors: list[str]
    stars: set[tuple[int, int]] = field(default_factory=set)

    def is_part(self) -> bool:
        return any(n != "." for n in self.neighbors)


def get_neighbors(i, j, lines):
    neighbors = []
    stars = set()
    MAX_J = len(lines[0]) - 1
    j_min = max(0, j - 1)
    j_max = min(MAX_J, j + 1)

    MAX_I = len(lines) - 1
    i_min = max(0, i - 1)
    i_max = min(MAX_I, i + 1)

    for i_ in range(i_min, i_max + 1):
        for j_ in range(j_min, j_max + 1):
            if i_ == i and j_ == j:
                continue
            n = lines[i_][j_]
            if not n.isdigit():
                neighbors.append(n)
                if n == "*":
                    stars.add((i_, j_))
    return neighbors, stars


def run(input_: str) -> int:
    lines = input_.splitlines()
    numbers = []
    num = ""
    neighbors = []
    stars = set()

    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            if char.isdigit():
                num += char
                n, s = get_neighbors(i, j, lines)
                neighbors.extend(n)
                stars.update(s)
            else:
                if num:
                    numbers.append(Number(int(num), neighbors, stars))
                    num = ""
                    neighbors = []
                    stars = set()
        if num:
            numbers.append(Number(int(num), neighbors, stars))
            num = ""
            neighbors = []
            stars = set()

    star2num = {s: set() for n in numbers for s in n.stars}
    for n in numbers:
        for s in n.stars:
            star2num[s].add(n.num)

    return sum(functools.reduce(operator.mul, nums) for _, nums in star2num.items() if len(nums) == 2)


INPUT = """\
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
"""
EXPECTED = 467835


@pytest.mark.parametrize(("input_", "expected"), ((INPUT, EXPECTED),))
def test_puzzle(input_, expected):
    assert run(input_) == expected


if __name__ == "__main__":
    input_ = read_input(INPUT_TXT)
    print(run(input_))
