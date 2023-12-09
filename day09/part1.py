import os

import pytest

from aoc.utils import read_input

INPUT_TXT = os.path.join(os.path.dirname(__file__), "input.txt")


def run(input_: str) -> int:
    values = []
    for line in input_.splitlines():
        history = [[int(n) for n in line.split()]]
        while not all(n == 0 for n in history[-1]):
            history.append([history[-1][i + 1] - history[-1][i] for i in range(len(history[-1]) - 1)])
        history[-1].append(0)

        for i in range(1, len(history)):
            history[-i - 1].append(history[-i - 1][-1] + history[-i][-1])

        values.append(history[0][-1])
    return sum(values)


INPUT = """\
0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45
"""
EXPECTED = 114


@pytest.mark.parametrize(("input_", "expected"), ((INPUT, EXPECTED),))
def test_puzzle(input_, expected):
    assert run(input_) == expected
    assert False


if __name__ == "__main__":
    input_ = read_input(INPUT_TXT)
    print(run(input_))
