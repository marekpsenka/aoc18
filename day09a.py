import fileinput

input = map(str.rstrip, fileinput.input())

player_part, point_part = next(input).split(" players; last marble is worth ")
num_players = int(player_part)
last_worth = int(point_part.split(" ")[0])

marbles = [0]
current_index = 0
scores = [0 for _ in range(num_players)]

for worth in range(1, last_worth + 1):
    if worth % 23 == 0:
        index_of_removed = (current_index - 7) % len(marbles)
        removed = marbles.pop(index_of_removed)
        current_index = index_of_removed % len(marbles)
        scores[(worth % num_players) - 1] += worth + removed
    else:
        dest_index = (current_index + 2) % len(marbles)
        marbles.insert(dest_index, worth)
        current_index = dest_index

print(max(scores))
