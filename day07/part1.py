import os
from collections import Counter
from functools import lru_cache

import pytest

from aoc.utils import read_input

INPUT_TXT = os.path.join(os.path.dirname(__file__), "input.txt")

CARDS = "23456789TJQKA"

@lru_cache
def get_score(hand: str):
    counts = Counter(Counter(hand).values())
    if counts == Counter({5: 1}): #Five of a kind
        return 7
    elif counts == Counter({4: 1, 1: 1}): #Four of a kind
        return 6
    elif counts == Counter({3: 1, 2: 1}): #Full house
        return 5
    elif counts == Counter({3: 1, 1: 2}): #Three of a kind
        return 4
    elif counts == Counter({2: 2, 1: 1}): #Two pair
        return 3
    elif counts == Counter({2: 1, 1: 3}): #One pair
        return 2
    elif counts == Counter({1: 5}): #High card
        return 1
    return 0

@lru_cache
def get_values(hand: str):
    return [CARDS.index(c) for c in hand]


def run(input_: str) -> int:
    hands = {}
    for line in  input_.splitlines():
        hand, score = line.split()
        score = int(score)
        hands[hand] = score
    hands = sorted(hands.items(), key=lambda kv: (get_score(kv[0]), *get_values(kv[0])))
    return sum([score * i for i, (_,score) in enumerate(hands, 1)])

INPUT = """\
32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483
"""
EXPECTED = 6440


@pytest.mark.parametrize(("input_", "expected"), ((INPUT, EXPECTED),))
def test_puzzle(input_, expected):
    assert run(input_) == expected


if __name__ == "__main__":
    input_ = read_input(INPUT_TXT)
    print(run(input_))
