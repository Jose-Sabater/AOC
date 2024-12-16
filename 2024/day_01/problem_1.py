import sys

input_path = sys.argv[1] if len(sys.argv) > 1 else "input.txt"


def solve_problem(path):
    with open(path) as f:
        text = f.read().splitlines()

    lst_1 = sorted([int(line.split("   ")[0]) for line in text])
    lst_2 = sorted([int(line.split("   ")[1]) for line in text])
    result = []
    for l, r in zip(lst_1, lst_2):
        result.append(abs(r - l))

    print(sum(result))


solve_problem(input_path)


# with re
# import re

# with open("./2024/day_1/test_1.txt") as f:
#     text = f.read().splitlines()

# # Using re groups
# pattern = r"(\d+)\s+(\d+)"
# for line in text:
#     match = re.search(pattern, line)
#     num_1 = match.group(1)
#     num_2 = match.group(2)
#     print(match)
#     print(num_1, num_2)

# print("#" * 25)
# # Using findall
# for line in text:
#     pattern = r"\d+"
#     results = re.findall(pattern, line)
#     if len(results) > 0:
#         print(results[0], results[1])
