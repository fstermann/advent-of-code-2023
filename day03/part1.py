import os
from dataclasses import dataclass

import pytest

from aoc.utils import read_input

INPUT_TXT = os.path.join(os.path.dirname(__file__), "input.txt")


@dataclass
class Number:
    num: int
    neighbors: list[str]

    def is_part(self) -> bool:
        return any(n != "." for n in self.neighbors)


def get_neighbors(i, j, lines):
    neighbors = []
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
    return neighbors


def run(input_: str) -> int:
    lines = input_.splitlines()
    numbers = []
    num = ""
    neighbors = []

    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            if char.isdigit():
                num += char
                neighbors.extend(get_neighbors(i, j, lines))
            else:
                if num:
                    numbers.append(Number(int(num), neighbors))
                    num = ""
                    neighbors = []
        if num:
            numbers.append(Number(int(num), neighbors))
            num = ""
            neighbors = []

    return sum(n.num for n in numbers if n.is_part())


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
EXPECTED = 4361


@pytest.mark.parametrize(("input_", "expected"), ((INPUT, EXPECTED),))
def test_puzzle(input_, expected):
    assert run(input_) == expected


if __name__ == "__main__":
    input_ = read_input(INPUT_TXT)
    print(run(input_))
