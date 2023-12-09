import os

import pytest

from aoc.utils import read_input

INPUT_TXT = os.path.join(os.path.dirname(__file__), "input.txt")


def run(input_: str) -> int:
    lines = input_.splitlines()
    instructions = lines[0]
    rules = {}
    for line in lines[2:]:
        rule, value = line.split(" = ")
        values = value.replace("(", "").replace(")", "").split(", ")
        rules[rule] = values

    node = "AAA"
    step = 0
    while node != "ZZZ":
        ixs = instructions[step % len(instructions)]
        node = rules[node][int(ixs == "R")]
        step += 1
    return step


INPUT_1 = """\
RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)
"""
EXPECTED_1 = 2
INPUT_2 = """\
LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)
"""
EXPECTED_2 = 6


@pytest.mark.parametrize(("input_", "expected"), [(INPUT_1, EXPECTED_1), (INPUT_2, EXPECTED_2)])
def test_puzzle(input_, expected):
    assert run(input_) == expected


if __name__ == "__main__":
    input_ = read_input(INPUT_TXT)
    print(run(input_))
