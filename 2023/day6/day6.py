import re
from functools import reduce

# with open("test.txt", "r") as f:
with open("input.txt", "r") as f:
    lines = f.read()

for i, line in enumerate(lines.split("\n")):
    if i == 0:
        times = re.findall(r"\d+", line)
        times = [int(time) for time in times]
    else:
        distances = re.findall(r"\d+", line)
        distances = [int(distance) for distance in distances]

print(times)
print(distances)

# Logic
best_dict = []
for i, time in enumerate(times):
    w = 0
    for t in range(time):
        speed = t
        movet = time - t
        dist = movet * t
        if dist > distances[i]:
            w += 1
    best_dict.append(w)

print(best_dict)
print(f"result 1 : {reduce(lambda x,y: x*y, best_dict)}")

# PART 2
time2 = ""
for time in times:
    time2 += str(time)
time2 = int(time2)
distance2 = ""
for distance in distances:
    distance2 += str(distance)
distance2 = int(distance2)
print("time2", time2)
print("distance2", distance2)
w = 0
for t in range(time2):
    speed = t
    movet = time2 - t
    dist = movet * t
    if dist > distance2:
        w += 1

print(f"Part 2 : {w}")
