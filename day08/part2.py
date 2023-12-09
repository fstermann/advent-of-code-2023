import math
import os

import pytest

from aoc.utils import read_input

INPUT_TXT = os.path.join(os.path.dirname(__file__), "input.txt")


def get_shortest_path(node: str, instructions: str, rules: dict[str, list[str]]) -> int:
    step = 0
    while not node.endswith("Z"):
        ixs = instructions[step % len(instructions)]
        node = rules[node][int(ixs == "R")]
        step += 1
    return step


def run(input_: str) -> int:
    lines = input_.splitlines()
    instructions = lines[0]
    rules = {}
    for line in lines[2:]:
        rule, value = line.split(" = ")
        values = value.replace("(", "").replace(")", "").split(", ")
        rules[rule] = values

    nodes = [node for node in rules if node.endswith("A")]
    shortest_paths = [get_shortest_path(node, instructions, rules) for node in nodes]
    return math.lcm(*shortest_paths)


INPUT = """\
LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)
"""
EXPECTED = 6


@pytest.mark.parametrize(("input_", "expected"), ((INPUT, EXPECTED),))
def test_puzzle(input_, expected):
    assert run(input_) == expected


if __name__ == "__main__":
    input_ = read_input(INPUT_TXT)
    print(run(input_))
