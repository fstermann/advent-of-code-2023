import os

import pytest

from aoc.utils import read_input

INPUT_TXT = os.path.join(os.path.dirname(__file__), "input.txt")

DIGITS = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


def get_first_digit(line: str) -> int:
    for i in range(1, len(line) + 1):
        if line[i - 1].isdigit():
            return int(line[i - 1])
        for letters, digit in DIGITS.items():
            if letters in line[:i]:
                return digit


def get_last_digit(line: str) -> int:
    for i in range(1, len(line) + 1):
        if line[-i].isdigit():
            return int(line[-i])
        for letters, digit in DIGITS.items():
            if letters in line[-i:]:
                return digit


def run(input_: str) -> int:
    sumx = 0
    for line in input_.splitlines():
        d1 = get_first_digit(line)
        d2 = get_last_digit(line)
        sumx += int(f"{d1}{d2}")
    return sumx


INPUT = """\
two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
"""
EXPECTED = 281


@pytest.mark.parametrize(("input_", "expected"), ((INPUT, EXPECTED),))
def test_puzzle(input_, expected):
    assert run(input_) == expected


if __name__ == "__main__":
    input_ = read_input(INPUT_TXT)
    print(run(input_))
