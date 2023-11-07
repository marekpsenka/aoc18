import fileinput
from dataclasses import dataclass


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

count = 0

for x in range(min_x, max_x + 1):
    for y in range(min_y, max_y + 1):
        if sum(manhattan(Point(x, y), p) for p in points) < 10000:
            count += 1

print(count)
