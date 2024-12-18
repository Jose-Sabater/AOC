import sys
from rich import print
import time
import re
from collections import deque

input_path = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

slots = open(input_path).read().split("\n\n")
added = 10_000_000_000_000
ratio = added / 100_000  # we select 100_000 for our work


# print(slots)
def get_smallest(A, B, dimension):
    if A[dimension] > B[dimension]:
        return B, A
    else:
        return A, B


f_t = []
for slot in slots:
    ax, bx = re.findall(r"X\+(\d+)", slot)
    ax, bx = int(ax), int(bx)
    ay, by = re.findall(r"Y\+(\d+)", slot)
    ay, by = int(ay), int(by)
    price_x = int(re.findall(r"X\=(\d+),", slot)[0])
    price_y = int(re.findall(r"Y\=(\d+)", slot)[0])
    A = {"x": ax, "y": ay, "t": 3}
    B = {"x": bx, "y": by, "t": 1}

    print(f"Price y {price_y} is smaller than Price x {price_x}")
    small, big = get_smallest(A, B, "y")

    # Initial floor and remainder
    floor = added // big["y"]
    rest = added % big["y"]
    effective_price_y = price_y + rest  # Start with the remainder added

    # Try decreasing floor if no solution is found
    while floor >= 0:
        t_l = []
        for n_big_y in range(effective_price_y // big["y"] + 1):
            remaining_price_y = effective_price_y - n_big_y * big["y"]
            if remaining_price_y % small["y"] == 0:
                n_small_y = remaining_price_y // small["y"]
                if n_small_y * small["x"] + n_big_y * big["x"] == price_x:
                    tokens = n_small_y * small["t"] + n_big_y * big["t"]
                    t_l.append(tokens)

        if t_l:
            f_t.append(min(t_l) + floor)
            break  # Solution found, move to the next slot
        else:
            # Adjust floor and effective price
            floor -= 1
            effective_price_y -= big["y"]

    if floor < 0:
        print(f"No solution found for slot: {slot}")

# P2
# do the same for a 100k and then multiply by the ration 1000000000/100k

print(f_t)
print(sum(f_t))
