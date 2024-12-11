import sys


# Using backtracking algoritm
input_path = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
with open(input_path) as f:
    text = f.read().strip()

sys.setrecursionlimit(10**6)
total = 0


def is_valid(target, ns):
    if len(ns) == 1:
        return ns[0] == target
    if is_valid(target, [ns[0] + ns[1]] + ns[2:]):
        return True
    if is_valid(target, [ns[0] * ns[1]] + ns[2:]):
        return True
    if is_valid(target, [int(str(ns[0]) + str(ns[1]))] + ns[2:]):
        return True
    return False


for line in text.strip().split("\n"):
    target, ns = line.strip().split(":")
    target = int(target)
    ns = [int(x) for x in ns.strip().split()]
    if is_valid(target, ns):
        total += target

print(total)
