import sys

input_path = sys.argv[1] if len(sys.argv) > 1 else "input.txt"


def solve(input):
    with open(input) as f:
        lines = f.read().splitlines()
    L = [list(map(int, line.split(" "))) for line in lines]
    counter = 0

    for l in L:
        inc_dec = l == sorted(l) or l == sorted(l, reverse=True)
        size_ok = True
        for i in range(len(l) - 1):
            if not 0 < abs(l[i] - l[i + 1]) <= 3:
                size_ok = False

        if inc_dec and size_ok:
            counter += 1
    print(counter)


solve(input_path)
