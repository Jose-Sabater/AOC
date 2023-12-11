import re

# with open("test.txt", "r") as f:
with open("day5.txt", "r") as f:
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
        seeds = [int(seed) for seed in seeds]
        continue

    maps = [map_ for map_ in group.split("\n")]
    # print(f"############{maps[0]}###########")
    # print(f"current seeds {seeds}")
    # loop through every mapping
    formulas = []
    for i in range(1, len(maps)):
        _nr = re.findall(r"\d+", maps[i])
        _nr = [int(j) for j in _nr]
        # print("maps", _nr)
        # [min,max,formula]
        form = [_nr[1], _nr[1] + _nr[2], _nr[0] - _nr[1]]
        formulas.append(form)
        # print("form", form)

    # Check if seeds are in the map and if such swap
    for i, seed in enumerate(seeds):
        # print(f"checking seed....{seed}")
        # print(f"Is {seed} > {form[0]} and < {form[1]}: {seed > form[1] } ")
        for form in formulas:
            if form[0] <= seed < form[1]:
                seeds[i] = seed + form[2]
                # print(f"im breaking {seed} -> {seed+form[2]}")
                break
    # print("seeds after the group")
    # print(seeds)
print("final_seed")
print(seeds)
print("smallest:")
print(min(seeds))
# THIS IS A working prototype but of course super slow
# Instead of calculating all the ranges make it so that it only calculates for the specific seed
