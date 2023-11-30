import fileinput

input = map(str.rstrip, fileinput.input())

serial = int(next(input))


def n_th_digit_from_back(i: int, n: int) -> int:
    s = str(i)
    if len(s) < n:
        return 0

    return int(s[-n])


def power_level(p: tuple[int, int], serial: int) -> int:
    rack_id = p[0] + 10
    power = rack_id * p[1]
    power += serial
    power *= rack_id
    return n_th_digit_from_back(power, 3) - 5


print(power_level((101, 153), 71))
