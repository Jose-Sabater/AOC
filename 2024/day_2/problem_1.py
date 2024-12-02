import sys

input_path = sys.argv[1] if len(sys.argv) > 1 else "input.txt"


def solve(input):
    with open(input) as f:
        lines = f.read().splitlines()
    L = [list(map(int, line.split(" "))) for line in lines]
    # L = [[int(l) for l in line.split(" ")] for line in lines]
    counter = 0

    for l in L:
        print(f"Evaluating {l}")
        skip = False
        # decreasing
        if l[0] > l[1]:
            for i in range(len(l) - 1):
                if l[i] - l[i + 1] > 3 or l[i] < l[i + 1] or l[i] == l[i + 1]:
                    skip = True
                    break
        # increasing
        elif l[0] < l[1]:
            for i in range(len(l) - 1):
                if l[i + 1] - l[i] > 3 or l[i] > l[i + 1] or l[i] == l[i + 1]:
                    skip = True
                    break
        else:
            continue
        if skip:
            continue
        print("Safe")
        counter += 1
    print(counter)


solve(input_path)
