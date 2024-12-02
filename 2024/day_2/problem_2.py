import sys
import logging

# logging.basicConfig(,level=sys.argv[2])

input_path = sys.argv[1] if len(sys.argv) > 1 else "input.txt"


def is_ok(lst):
    inc_dec = lst == sorted(lst) or lst == sorted(lst, reverse=True)
    size_ok = True
    for i in range(len(lst) - 1):
        if not 0 < abs(lst[i] - lst[i + 1]) <= 3:
            size_ok = False

    if inc_dec and size_ok:
        return True


def solve(input_path: str):
    with open(input_path) as f:
        lines = f.read().splitlines()

    L = [list(map(int, line.split(" "))) for line in lines]
    counter = 0
    for idx, l in enumerate(L):
        logging.info(f"Evaluating {l}")
        logging.error(f"there was an error {idx}: {l}")
        if is_ok(l):
            counter += 1
        else:
            for i in range(len(l)):
                tmp = l.copy()
                tmp.pop(i)
                if is_ok(tmp):
                    counter += 1
                    break
    print(counter)


solve(input_path)
