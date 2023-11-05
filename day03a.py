import fileinput
from collections import namedtuple, Counter

input = map(str.rstrip, fileinput.input())

Rectangle = namedtuple("Rectangle", ["left", "top", "width", "height"])


def parse_rectangle(line: str) -> Rectangle:
    _, right_part = line.split(" @ ")
    left_top_part, width_height_part = right_part.split(": ")
    left_str, top_str = left_top_part.split(",")
    width_str, height_str = width_height_part.split("x")
    return Rectangle(
        int(left_str), int(top_str), int(width_str), int(height_str)
    )


fabric = Counter()

for rect in map(parse_rectangle, input):
    for i in range(rect.height):
        for j in range(rect.width):
            fabric[(rect.top + i, rect.left + j)] += 1

print(len(list(filter(lambda x: x > 1, fabric.values()))))
