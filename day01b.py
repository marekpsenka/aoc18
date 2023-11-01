import fileinput
import itertools

input = map(str.rstrip, fileinput.input())

seen = set()
value = 0

for change in itertools.cycle(map(int, input)):
    value += change
    if value in seen:
        break
    seen.add(value)

print(value)
