import os

import pytest

from aoc.utils import read_input

INPUT_TXT = os.path.join(os.path.dirname(__file__), "input.txt")


def run(input_: str) -> int:
    times = [int(t) for t in input_.splitlines()[0].split(": ")[1].split()]
    distances = [int(d) for d in input_.splitlines()[1].split(": ")[1].split()]
    result = 1

    for time, distance in zip(times, distances):
        options = [(time - i) * i for i in range(time+1)]
        result *= sum([o > distance for o in options])
    return result


INPUT = """\
Time:      7  15   30
Distance:  9  40  200
"""
EXPECTED = 288


@pytest.mark.parametrize(("input_", "expected"), ((INPUT, EXPECTED),))
def test_puzzle(input_, expected):
    assert run(input_) == expected


if __name__ == "__main__":
    input_ = read_input(INPUT_TXT)
    print(run(input_))
