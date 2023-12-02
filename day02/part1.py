import os
from dataclasses import dataclass

import pytest

from aoc.utils import read_input

INPUT_TXT = os.path.join(os.path.dirname(__file__), "input.txt")

RED_CUBES = 12
GREEN_CUBES = 13
BLUE_CUBES = 14


@dataclass
class CubeSet:
    red: int = 0
    green: int = 0
    blue: int = 0

    def is_valid(self, red_cubes: int, green_cubes: int, blue_cubes: int) -> bool:
        return red_cubes >= self.red and green_cubes >= self.green and blue_cubes >= self.blue


@dataclass
class Game:
    idx: int
    cubesets: list[CubeSet]


def parse_game(line: str) -> Game:
    line = line.replace("Game ", "")
    idx, cubes = line.split(": ")
    cube_sets = cubes.split("; ")
    cube_sets = [[c.split() for c in cs.split(", ")] for cs in cube_sets]
    cubes = [CubeSet(**{color: int(num) for num, color in cs}) for cs in cube_sets]
    return Game(int(idx), cubes)


def run(input_: str) -> int:
    games = [parse_game(line) for line in input_.splitlines()]
    valid_ids = set()
    for game in games:
        if all(cube_set.is_valid(RED_CUBES, GREEN_CUBES, BLUE_CUBES) for cube_set in game.cubesets):
            valid_ids.add(game.idx)
    return sum(valid_ids)


INPUT = """\
Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
"""
EXPECTED = 8


@pytest.mark.parametrize(("input_", "expected"), ((INPUT, EXPECTED),))
def test_puzzle(input_, expected):
    assert run(input_) == expected


if __name__ == "__main__":
    input_ = read_input(INPUT_TXT)
    print(run(input_))
