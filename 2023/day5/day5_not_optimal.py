import re

with open("test.txt", "r") as f:
    # with open("day5.txt", "r") as f:
    lines = f.read()


# seeds = re.findall(r"\d+", lines.split("seed-to-soil")[0])
# print(seeds)

# two options we either map all the nrs inside a dict
# or we map the formula inside a dict and then only use it for the seeds

groups = [group for group in lines.split("\n\n")]
# print(groups)
# seeds = re.findall(r"\d+", groups[0])

for i, group in enumerate(groups):
    if i == 0:
        seeds = re.findall(r"\d+", group)
        continue
    maps = [map_ for map_ in group.split("\n")]
    print(maps[0])
    # loop through every mapping
    map_dict = {}
    for i in range(1, len(maps)):
        _nr = re.findall(r"\d+", maps[i])
        for j in range(len(_nr)):
            _nr[j] = int(_nr[j])
        print(_nr)
        for k in range(_nr[2]):
            map_dict[k + _nr[1]] = _nr[1] - (_nr[1] - _nr[0]) + k
    print(map_dict)

    # Check if seeds are in the map and if such swap
    for i, seed in enumerate(seeds):
        if int(seed) in map_dict:
            seeds[i] = map_dict[int(seed)]
    print("seeds after the group")
    print(seeds)
print("final_seed")
print(seeds)
# THIS IS A working prototype but of course super slow
# Instead of calculating all the ranges make it so that it only calculates for the specific seed
