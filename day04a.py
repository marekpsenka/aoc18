import fileinput
from collections import namedtuple, defaultdict, Counter
from dataclasses import dataclass
from datetime import datetime


@dataclass
class FallsAsleep:
    pass


@dataclass
class WakesUp:
    pass


@dataclass
class BeginsShift:
    id: int


Event = FallsAsleep | WakesUp | BeginsShift

input = map(str.rstrip, fileinput.input())

Record = namedtuple("Record", ["datetime", "event"])


def parse_record(line: str) -> Record:
    datetime_part, event_part = line.split("] ")
    dt = datetime.strptime(datetime_part[1:], "%Y-%m-%d %H:%M")
    match event_part:
        case "falls asleep":
            return Record(dt, FallsAsleep())
        case "wakes up":
            return Record(dt, WakesUp())
        case _:
            _, part_with_id = event_part.split("#")
            return Record(dt, BeginsShift(int(part_with_id.split()[0])))


records = sorted(map(parse_record, input), key=lambda r: r.datetime)
records_iter = iter(records)
this_id = next(records_iter).event.id
minutes = defaultdict(Counter)

while True:
    try:
        match next(records_iter):
            case Record(dt, FallsAsleep()):
                match next(records_iter):
                    case Record(dt2, WakesUp()):
                        for i in range(dt.minute, dt2.minute):
                            minutes[this_id][i] += 1
                    case _:
                        raise RuntimeError("Wakes up record was expected")
            case Record(_, BeginsShift(i)):
                this_id = i
    except StopIteration:
        break

sleepy_guard_id = max(minutes.items(), key=lambda p: sum(p[1].values()))[0]
chosen_minute = max(minutes[sleepy_guard_id].items(), key=lambda p: p[1])[0]

print(sleepy_guard_id * chosen_minute)
