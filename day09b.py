import fileinput
from collections import deque

input = map(str.rstrip, fileinput.input())

player_part, point_part = next(input).split(" players; last marble is worth ")
num_players = int(player_part)
last_worth = int(point_part.split(" ")[0])

marbles = deque([0])
scores = [0 for _ in range(num_players)]

for worth in range(1, last_worth + 1):
    if worth % 23 == 0:
        marbles.rotate(7)
        scores[(worth % num_players) - 1] += worth + marbles.pop()
        marbles.rotate(-1)
    else:
        marbles.rotate(-1)
        marbles.append(worth)

print(max(scores))
