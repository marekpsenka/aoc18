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

last_diff = 0
for k in range(50000000000):
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

    diff = sum(new_state) - sum(state)
    if diff == last_diff:
        print(k)
        print(last_diff)
        print(((50000000000 - k) * last_diff) + sum(state))
        break

    state = new_state
    last_diff = diff
