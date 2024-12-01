with open("day4.txt", "r") as f:
    # with open("test.txt", "r") as f:
    lines = f.read()
import re

regex = r"\d+"
result_1 = 0
for i, line in enumerate(lines.split("\n")):
    pre, aftr = line.split("|")
    nrs = re.findall(regex, aftr)
    winners = re.findall(regex, pre.split(":")[1])
    v = 0
    for nr in nrs:
        if nr in winners:
            if v == 0:
                v = 1
            else:
                v *= 2
    print(f"card{i}'s value is {v}")
    result_1 += v

print(result_1)
