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

max_total_power = 0
max_coords = None

for y in range(1, 299):
    for x in range(1, 299):
        total_power = 0
        for j in [-1, 0, 1]:
            for i in [-1, 0, 1]:
                total_power += grid[y + j][x + i]

        if total_power > max_total_power:
            max_total_power = total_power
            max_coords = (x, y)

print(max_coords)
