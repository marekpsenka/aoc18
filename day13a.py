import fileinput
from enum import Enum, IntEnum, auto
from dataclasses import dataclass


class Direction(Enum):
    Up = auto()
    Down = auto()
    Left = auto()
    Right = auto()

    def opposite(self) -> "Direction":
        match self:
            case Direction.Up:
                return Direction.Down
            case Direction.Down:
                return Direction.Up
            case Direction.Right:
                return Direction.Left
            case Direction.Left:
                return Direction.Right

    def turn_left(self) -> "Direction":
        match self:
            case Direction.Up:
                return Direction.Left
            case Direction.Down:
                return Direction.Right
            case Direction.Right:
                return Direction.Up
            case Direction.Left:
                return Direction.Down

    def turn_right(self) -> "Direction":
        match self:
            case Direction.Up:
                return Direction.Right
            case Direction.Down:
                return Direction.Left
            case Direction.Right:
                return Direction.Down
            case Direction.Left:
                return Direction.Up


class IntersectionBhv(IntEnum):
    TurnLeft = 0
    ContinueStraight = 1
    TurnRight = 2

    def next(self) -> "IntersectionBhv":
        return IntersectionBhv((self + 1) % 3)


@dataclass
class State:
    dir: Direction
    bhv: IntersectionBhv


Point = tuple[int, int]


def move(p: Point, dir: Direction) -> Point:
    match dir:
        case Direction.Up:
            return (p[0] - 1, p[1])
        case Direction.Down:
            return (p[0] + 1, p[1])
        case Direction.Left:
            return (p[0], p[1] - 1)
        case Direction.Right:
            return (p[0], p[1] + 1)


def transform_direction(prev: Direction, tile: str) -> Direction:
    match tile:
        case "\\":
            match prev:
                case Direction.Left:
                    return Direction.Up
                case Direction.Right:
                    return Direction.Down
                case Direction.Up:
                    return Direction.Left
                case Direction.Down:
                    return Direction.Right
        case "/":
            match prev:
                case Direction.Left:
                    return Direction.Down
                case Direction.Right:
                    return Direction.Up
                case Direction.Up:
                    return Direction.Right
                case Direction.Down:
                    return Direction.Left
        case "-":
            if prev == Direction.Left or prev == Direction.Right:
                return prev
            else:
                raise RuntimeError
        case "|":
            if prev == Direction.Up or prev == Direction.Down:
                return prev
            else:
                raise RuntimeError
        case _:
            raise RuntimeError


def transform_state(prev: State, tile: str) -> State:
    if tile == "+":
        match prev.bhv:
            case IntersectionBhv.TurnLeft:
                return State(prev.dir.turn_left(), prev.bhv.next())
            case IntersectionBhv.ContinueStraight:
                return State(prev.dir, prev.bhv.next())
            case IntersectionBhv.TurnRight:
                return State(prev.dir.turn_right(), prev.bhv.next())
            case _:
                raise RuntimeError
    else:
        return State(transform_direction(prev.dir, tile), prev.bhv)


input = list(map(lambda li: li[: len(li) - 1], map(list, fileinput.input())))
carts: dict[Point, State] = dict()

for y in range(len(input)):
    for x in range(len(input[0])):
        match input[y][x]:
            case ">":
                carts[(y, x)] = State(
                    Direction.Right, IntersectionBhv.TurnLeft
                )
                input[y][x] = "-"
            case "<":
                carts[(y, x)] = State(Direction.Left, IntersectionBhv.TurnLeft)
                input[y][x] = "-"
            case "^":
                carts[(y, x)] = State(Direction.Up, IntersectionBhv.TurnLeft)
                input[y][x] = "|"
            case "v":
                carts[(y, x)] = State(Direction.Down, IntersectionBhv.TurnLeft)
                input[y][x] = "|"

crash_found = False
while not crash_found:
    moved_carts: dict[Point, State] = dict()
    for pos in list(carts.keys()):
        st = carts.pop(pos)
        new_pos = move(pos, st.dir)
        if new_pos in carts or new_pos in moved_carts:
            print(new_pos)
            crash_found = True
            break

        moved_carts[new_pos] = transform_state(
            st, input[new_pos[0]][new_pos[1]]
        )

    carts = moved_carts
