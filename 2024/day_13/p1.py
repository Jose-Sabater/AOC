import sys
from rich import print
import time
import re
from collections import deque

input_path = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

slots = open(input_path).read().split("\n\n")


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
    # the optimal is always when you use the largest number first. And then find the largest combination of largest num so that whats left is taken by second largest
    # deltas

    print(f"Price y {price_y} is smaller than Price x {price_x} ")
    small, big = get_smallest(A, B, "y")
    # print(small, big)
    # print(min_y)
    t_l = []
    for i, num in enumerate(range(0, price_y, small["y"])):
        if (price_y - num) % big["y"] == 0:
            # check if the other side also matches
            n_small_y = i
            n_big_y = (price_y - num) // big["y"]
            if n_small_y * small["x"] + n_big_y * big["x"] == price_x:
                tokens = n_small_y * small["t"] + n_big_y * big["t"]
                t_l.append(tokens)
    print(t_l)
    if t_l != []:
        f_t.append(min(t_l))

print(f_t)
print(sum(f_t))
