import sys
from rich import print
import time
from collections import Counter

input_path = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

text = open(input_path).read()


# make into iterator to return 1 by 1
def change(num):
    if num == 0:
        yield 1
    elif len(str(num)) % 2 == 0:
        left = int(str(num)[0 : len(str(num)) // 2])
        right = int(str(num)[len(str(num)) // 2 :])
        yield left
        yield right
    else:
        yield num * 2024


# loop through the current counter and change the stones
def blink(hm, rounds):
    for _ in range(rounds):
        start = time.time()
        print("Start round", _)
        # print(hm)
        new_hm = Counter()
        for num, size in hm.items():
            for new_num in change(
                num
            ):  # returns 1 item per loop , so for the split will return twice
                new_hm[
                    new_num
                ] += size  # adds all times this number shows, so if the number was twice, we can expect this result twice, without computing it
        hm = new_hm
        print("total time in round:", time.time() - start)
    return hm


# Create a hashmap, use Counter for this
start = time.time()
hm = Counter(map(int, text.split()))
hm = blink(hm, 75)
print("iterative result", sum(hm.values()))
print("total time:", time.time() - start)

# recursive solution
hm = {}

sys.setrecursionlimit(10**6)


def solve(num, rounds):
    if (num, rounds) in hm:
        return hm[(num, rounds)]

    if rounds == 0:
        ret = 1

    elif num == 0:
        ret = solve(1, rounds - 1)

    elif len(str(num)) % 2 == 0:
        left = int(str(num)[0 : len(str(num)) // 2])
        right = int(str(num)[len(str(num)) // 2 :])
        ret = solve(left, rounds - 1) + solve(right, rounds - 1)
    else:
        ret = solve(num * 2024, rounds - 1)

    hm[(num, rounds)] = ret
    return ret


# print(sum(solve(map(int, text.split()), 5)))
total = 0
start = time.time()
for num in text.split():
    total += solve(int(num), 75)

print("recursion result:", total)
print("total time", time.time() - start)
