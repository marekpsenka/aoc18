import fileinput
from more_itertools import locate


def read_rule(line: str) -> tuple[str, str]:
    left, right = line.split(" => ")
    return (left, right)


input = map(str.rstrip, fileinput.input())

_, initial_state_str = next(input).split(": ")
state = set(locate(initial_state_str, lambda x: x == "#"))

_ = next(input)
rules = dict(map(read_rule, input))

for _ in range(20):
    new_state = set()
    for i in range(min(state) - 3, max(state) + 3):
        neighborhood = "".join(
            [
                "#" if i - 2 in state else ".",
                "#" if i - 1 in state else ".",
                "#" if i in state else ".",
                "#" if i + 1 in state else ".",
                "#" if i + 2 in state else ".",
            ]
        )

        if neighborhood in rules and rules[neighborhood] == "#":
            new_state.add(i)

    state = new_state

print(sum(state))
