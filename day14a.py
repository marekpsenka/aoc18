import fileinput

input = map(str.rstrip, fileinput.input())

req = int(next(input))

scores = [3, 7]
e1 = 0
e2 = 1

for i in range(req + 10):
    sum_str = str(scores[e1] + scores[e2])
    scores.append(int(sum_str[0]))
    if len(sum_str) == 2:
        scores.append(int(sum_str[1]))
    e1 = (e1 + scores[e1] + 1) % len(scores)
    e2 = (e2 + scores[e2] + 1) % len(scores)
    if e1 == e2:
        e2 = (e1 + 1) % len(scores)

print("".join(map(str, scores[req : (req + 10)])))
