import fileinput
from collections import namedtuple, defaultdict

input = map(str.rstrip, fileinput.input())

Rectangle = namedtuple("Rectangle", ["id", "left", "top", "width", "height"])


def parse_rectangle(line: str) -> Rectangle:
    id_part, right_part = line.split(" @ ")
    left_top_part, width_height_part = right_part.split(": ")
    left_str, top_str = left_top_part.split(",")
    width_str, height_str = width_height_part.split("x")
    return Rectangle(
        id_part, int(left_str), int(top_str), int(width_str), int(height_str)
    )


rects = list(map(parse_rectangle, input))
candidate_ids = set(rect.id for rect in rects)
fabric = defaultdict(list)

for rect in rects:
    for i in range(rect.height):
        for j in range(rect.width):
            fabric[(rect.top + i, rect.left + j)].append(rect.id)

for val in fabric.values():
    if len(val) > 1:
        for id in val:
            if id in candidate_ids:
                candidate_ids.remove(id)

print(candidate_ids)
