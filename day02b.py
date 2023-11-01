import fileinput
import itertools

input = map(str.rstrip, fileinput.input())

for [left, right] in itertools.combinations(input, 2):
    common = list(filter(lambda p: p[0] == p[1], zip(left, right)))
    if len(common) == len(left) - 1:
        print("".join(map(lambda p: p[0], common)))
