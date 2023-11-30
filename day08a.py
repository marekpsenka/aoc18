import fileinput
from dataclasses import dataclass
from typing import List, Tuple


@dataclass
class Node:
    children: List["Node"]
    metadata: List[int]

    def sum_metadata(self) -> int:
        return sum(self.metadata) + sum(
            child.sum_metadata() for child in self.children
        )


def parse_node(cursor: int, numbers: List[int]) -> Tuple[Node, int]:
    num_children = numbers[cursor]
    num_metadata = numbers[cursor + 1]
    children = []
    temp_cursor = cursor + 2
    for _ in range(num_children):
        (new_child, temp_cursor) = parse_node(temp_cursor, numbers)
        children.append(new_child)

    return (
        Node(children, numbers[temp_cursor : (temp_cursor + num_metadata)]),
        temp_cursor + num_metadata,
    )


input = map(str.rstrip, fileinput.input())

numbers = list(map(int, next(input).split(" ")))

root, _ = parse_node(0, numbers)
print(root.sum_metadata())
