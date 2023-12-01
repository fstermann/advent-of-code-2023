import os

import pytest

from aoc.utils import read_input

INPUT_TXT = os.path.join(os.path.dirname(__file__), "input.txt")


def run(input_: str) -> int:
    sumx = 0
    for line in input_.splitlines():
        digits = [n for n in line if n.isdigit()]
        sumx += int(f"{digits[0]}{digits[-1]}")
    return sumx


INPUT = """\
1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
"""
EXPECTED = 142


@pytest.mark.parametrize(("input_", "expected"), ((INPUT, EXPECTED),))
def test_puzzle(input_, expected):
    assert run(input_) == expected


if __name__ == "__main__":
    input_ = read_input(INPUT_TXT)
    print(run(input_))
