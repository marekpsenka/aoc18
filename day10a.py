import fileinput
import re
from dataclasses import dataclass
from typing import Tuple, Set
from operator import itemgetter

input = map(str.rstrip, fileinput.input())


@dataclass
class Star:
    pos: Tuple[int, int]
    vel: Tuple[int, int]


def parse_star(line: str) -> Star:
    pos_match, vel_match = re.findall(r"<( *-?\d+), ( *-?\d+)>", line)
    return Star(
        pos=(int(pos_match[0]), int(pos_match[1])),
        vel=(int(vel_match[0]), int(vel_match[1])),
    )


def add(a: Tuple[int, int], b: Tuple[int, int]) -> Tuple[int, int]:
    return (a[0] + b[0], a[1] + b[1])


def times(k: int, a: Tuple[int, int]) -> Tuple[int, int]:
    return (k * a[0], k * a[1])


def field_width(positions: Set[Tuple[int, int]]) -> Tuple[int, int]:
    min_y = min(positions, key=itemgetter(1))[1]
    max_y = max(positions, key=itemgetter(1))[1]
    return (max_y - min_y, min_y)


def field_height(positions: Set[Tuple[int, int]]) -> Tuple[int, int]:
    min_x = min(positions, key=itemgetter(0))[0]
    max_x = max(positions, key=itemgetter(0))[0]
    return (max_x - min_x, min_x)


in_stars = [parse_star(line) for line in input]

positions = set(star.pos for star in in_stars)
width, min_y = field_width(positions)
time = 0

while True:
    new_positions = set(
        add(star.pos, times(time, star.vel)) for star in in_stars
    )
    new_width, new_min_y = field_width(new_positions)
    if new_width > width:
        height, min_x = field_height(positions)
        for j in range(width + 1):
            for i in range(height + 1):
                if (i + min_x, j + min_y) in positions:
                    print("#", end="")
                else:
                    print(".", end="")
            print("")
        break

    width = new_width
    min_y = new_min_y
    positions = new_positions
    time += 1
