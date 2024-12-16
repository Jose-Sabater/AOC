import sys
from rich import print
from collections import deque

input_path = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

text = open(input_path).read()


ret = []  # final list

# go through numbers 1 by 1 and create a list of strings that will be appended to the return list
reps = 1
nums = [num for num in text.split(" ")]


def solve(num, rounds):
    temp = [num]
    i = 0
    while i < rounds:
        new_l = []
        for num in temp:
            if num == "0":
                new_l.append("1")
            elif len(num) % 2 == 0:
                left = num[0 : (len(num) // 2)]
                right = num[(len(num) // 2) :]
                new_l.append(left)
                new_l.append(str(int(right)))
            else:
                new_l.append(str(int(num) * 2024))
        temp = new_l
        i += 1
    return temp


for i, num in enumerate(nums):

    ret += solve(num, 25)

# print(ret)
print(len(ret))
