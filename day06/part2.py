import os

import pytest

from aoc.utils import read_input

INPUT_TXT = os.path.join(os.path.dirname(__file__), "input.txt")


def run(input_: str) -> int:
    time = int(input_.splitlines()[0].split(": ")[1].replace(" ", ""))
    distance = int(input_.splitlines()[1].split(": ")[1].replace(" ", ""))
    options = [(time - i) * i for i in range(time+1)]
    return sum([o > distance for o in options])


INPUT = """\
Time:      7  15   30
Distance:  9  40  200
"""
EXPECTED = 71503


@pytest.mark.parametrize(("input_", "expected"), ((INPUT, EXPECTED),))
def test_puzzle(input_, expected):
    assert run(input_) == expected


if __name__ == "__main__":
    input_ = read_input(INPUT_TXT)
    print(run(input_))
