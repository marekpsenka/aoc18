import fileinput
from collections import defaultdict
from itertools import islice
from typing import Set, Tuple, List


def duration(c: str) -> int:
    return ord(c) - 65 + 60 + 1


num_workers = 5

input = map(str.rstrip, fileinput.input())

deps = defaultdict(list)
all_tasks = set()

for line in input:
    left, right = line.split(" must be finished before step ")
    deps[right[0]].append(left[-1])
    all_tasks.add(right[0])
    all_tasks.add(left[-1])


def ensure_allocation(unblocked: Set[str], in_progress: List[Tuple[int, str]]):
    starting = islice(sorted(unblocked), num_workers - len(in_progress))
    for task in starting:
        unblocked.remove(task)
        in_progress.append((duration(task), task))


unblocked = all_tasks.difference(set(deps.keys()))
in_progress = []
ensure_allocation(unblocked, in_progress)

order = []
elapsed = 0

while not len(in_progress) == 0:
    executed = min(in_progress)
    in_progress.remove(executed)
    elapsed += executed[0]
    in_progress = [(task[0] - executed[0], task[1]) for task in in_progress]

    newly_unblocked = []
    for task, dependencies in deps.items():
        if executed[1] in dependencies:
            dependencies.remove(executed[1])
        if len(dependencies) == 0:
            newly_unblocked.append(task)

    for task in newly_unblocked:
        unblocked.add(task)
        deps.pop(task)

    ensure_allocation(unblocked, in_progress)

    order.append(executed[1])

print("".join(order))
print(elapsed)
