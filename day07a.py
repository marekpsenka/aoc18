import fileinput
from collections import defaultdict

input = map(str.rstrip, fileinput.input())

deps = defaultdict(list)
all_tasks = set()

for line in input:
    left, right = line.split(" must be finished before step ")
    deps[right[0]].append(left[-1])
    all_tasks.add(right[0])
    all_tasks.add(left[-1])

unblocked = all_tasks.difference(set(deps.keys()))

order = []

while not len(unblocked) == 0:
    executed = min(unblocked)
    unblocked.remove(executed)
    newly_unblocked = []
    for task, dependencies in deps.items():
        if executed in dependencies:
            dependencies.remove(executed)
        if len(dependencies) == 0:
            newly_unblocked.append(task)

    for task in newly_unblocked:
        unblocked.add(task)
        deps.pop(task)

    order.append(executed)

print("".join(order))
