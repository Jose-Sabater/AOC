import sys
import re
from itertools import combinations

input_path = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
with open(input_path) as f:
    text = f.read()


# 1 possible operations *, +
# 2 + +, + *, * +, * *
# 3 +++, ++*, +**, ***, **+, *++, *+*, +*+, 2^n
simbols = "*+="


def get_combinations_list(size):
    simbols_comb = simbols
    for i in range(size - 1):
        simbols_comb += "*+="
    # print(simbols_comb)
    combs = combinations(simbols_comb, size)
    return list(set([comb for comb in combs]))


def run_operation(sign, nums):
    # print(f"runing operation for: {sign}, {nums}")
    if sign == "+":
        return sum(nums)
    if sign == "*":
        return nums[0] * nums[1]
    if sign == "=":
        return int(str(nums[0]) + str(nums[1]))


total = 0
for line in text.split("\n"):
    # print(f"Starting line {line}")
    result = int(line.split(":")[0])
    operators = line.split(": ")[1].split(" ")
    operators = list(map(int, operators))
    n_operations = len(operators) - 1
    # print(result)
    # print(operators)
    # print(n_operations)

    # possible combinations
    comb_list = get_combinations_list(n_operations)
    # print(comb_list)
    skip = False
    for comb in comb_list:
        # print(f"starting combination: {comb}")
        r = 0
        for i, sign in enumerate(comb):
            if i == 0:
                r = run_operation(sign, operators[i : i + 2])
            else:
                r = run_operation(sign, [r, operators[i + 1]])
            # print(f"r is equal to{r}")
        if r == result:
            # print("SUCCESS!!!!")
            total += result
            # print("total: ", total)
            skip = True
            break
        if skip:
            break


print(total)
