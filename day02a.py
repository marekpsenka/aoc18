import fileinput
from collections import Counter

input = map(str.rstrip, fileinput.input())

has_two = 0
has_three = 0

for c in map(Counter, input):
    if any(map(lambda x: x == 2, c.values())):
        has_two += 1
    if any(map(lambda x: x == 3, c.values())):
        has_three += 1

print(has_two * has_three)
