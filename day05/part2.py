import os

import pytest

from aoc.utils import read_input

INPUT_TXT = os.path.join(os.path.dirname(__file__), "input.txt")


def batch_tuples(iterable, n: int = 1):
    length = len(iterable)
    for ndx in range(0, length, n):
        yield tuple(iterable[ndx : min(ndx + n, length)])


def get_maps(lines: list[str]) -> list[list[tuple[int, int, int]]]:
    maps = []
    new_map = []
    for line in lines:
        if line:
            if line[0].isdigit():
                new_map.append([int(s) for s in line.split()])
        else:
            maps.append(new_map)
            new_map = []
    maps.append(new_map)
    return maps


def run(input_: str) -> int:
    lines = input_.splitlines()
    # seeds = [int(s) for s in lines[0].split(": ")[1].split()][::2]
    seeds = batch_tuples([int(s) for s in lines[0].split(": ")[1].split()], n=2)
    seeds = [sx for s1, s2 in seeds for sx in list(range(s1, s1 + s2))]
    # seeds = [sx for s1, s2 in seeds for sx in (s1, s1 + s2 - 1)]
    maps = get_maps(lines[2:])
    print(len(seeds))
    exit()
    seed_loc_cache = {}

    locations = []
    for seed in seeds:
        if seed in seed_loc_cache:
            continue
        location = seed
        for map_ in maps:
            for dest, source, length in map_:
                if source <= location < (source + length):
                    location = location + dest - source
                    break
        locations.append(location)
        seed_loc_cache[seed] = location
    return min(locations)


INPUT = """\
seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4
"""
EXPECTED = 46


@pytest.mark.parametrize(("input_", "expected"), ((INPUT, EXPECTED),))
def test_puzzle(input_, expected):
    assert run(input_) == expected


if __name__ == "__main__":
    input_ = read_input(INPUT_TXT)
    print(run(input_))
