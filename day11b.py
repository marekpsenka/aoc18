import fileinput

input = map(str.rstrip, fileinput.input())

serial = int(next(input))


def n_th_digit_from_back(i: int, n: int) -> int:
    s = str(i)
    if len(s) < n:
        return 0

    return int(s[-n])


def power_level(x: int, y: int, serial: int) -> int:
    rack_id = x + 10
    power = rack_id * y
    power += serial
    power *= rack_id
    return n_th_digit_from_back(power, 3) - 5


grid = [
    [power_level(x + 1, y + 1, serial) for x in range(300)] for y in range(300)
]

sat = [[0 for x in range(300)] for y in range(300)]

for y in range(300):
    for x in range(300):
        sat[y][x] += grid[y][x]
        if y > 0:
            sat[y][x] += sat[y - 1][x]
            if x > 0:
                sat[y][x] -= sat[y - 1][x - 1]
        if x > 0:
            sat[y][x] += sat[y][x - 1]

max_total_power = 0
max_coords = None

for y in range(300):
    for x in range(300):
        for n in range(300 - max(x, y)):
            total_power = (
                sat[y][x] + sat[y + n][x + n] - sat[y][x + n] - sat[y + n][x]
            )

            if total_power > max_total_power:
                max_total_power = total_power
                max_coords = (x + 1, y + 1, n)

print(max_coords)
