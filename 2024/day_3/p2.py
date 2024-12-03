import re
import sys

input_path = sys.argv[1] if len(sys.argv) > 1 else "input.txt"


def solve(input):
    with open(input_path) as f:
        text = f.read()

    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"  # looking at output the size of the numbers is always between 1 and 3
    pattern = re.compile(pattern)

    total = 0
    # Initial conditions
    start = 0
    end = text.find("don't()")  # find returns -1 if not found
    while True:
        for match in pattern.finditer(text, start, end if end != -1 else len(text)):
            total += int(match.group(1)) * int(match.group(2))

        if end == -1:
            break

        start = text.find(
            "do()", end
        )  # use the end of the previous loop as starting point
        end = text.find("don't()", start)  # use the start as starting point for the end

    print(total)


solve(input_path)
