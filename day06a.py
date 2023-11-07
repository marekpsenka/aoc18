import fileinput
from dataclasses import dataclass
from collections import defaultdict
from operator import itemgetter


@dataclass(frozen=True)
class Point:
    x: int
    y: int


def parse_point(line: str) -> Point:
    x_str, y_str = line.split(", ")
    return Point(int(x_str), int(y_str))


def manhattan(p1: Point, p2: Point) -> int:
    return abs(p1.x - p2.x) + abs(p1.y - p2.y)


input = map(str.rstrip, fileinput.input())
points = list(map(parse_point, input))

min_x = min(points, key=lambda p: p.x).x
min_y = min(points, key=lambda p: p.y).y
max_x = max(points, key=lambda p: p.x).x
max_y = max(points, key=lambda p: p.y).y

counts = defaultdict(int)
infinite = set()

for x in range(min_x, max_x + 1):
    for y in range(min_y, max_y + 1):
        dist_data = sorted(
            [(manhattan(Point(x, y), p), p) for p in points], key=itemgetter(0)
        )
        if dist_data[0][0] != dist_data[1][0]:
            counts[dist_data[0][1]] += 1
            if x == max_x or y == max_y or x == min_x or y == min_y:
                infinite.add(dist_data[0][1])

for inf_point in infinite:
    counts.pop(inf_point)

print(max(counts.values()))
