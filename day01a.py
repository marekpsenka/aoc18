import fileinput

input = map(str.rstrip, fileinput.input())

print(sum(map(int, input)))
