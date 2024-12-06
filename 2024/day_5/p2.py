import sys

input_path = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
with open(input_path) as f:
    text = f.read()

rules, checks = text.split("\n\n")
rule_dict = {}
for row in rules.splitlines():
    x, y = map(int, row.split("|"))
    rule_dict.setdefault(x, []).append(y)

# rows to check
C = [[int(r) for r in row.split(",")] for row in checks.splitlines()]
print(rule_dict)


def check_and_reorder(rule_dict, og_list):
    lst = og_list.copy()
    good = True
    rerun = True
    while rerun:
        rerun = False
        for i, num in enumerate(lst):
            rules = rule_dict.get(num, [])
            for j, c_num in enumerate(rules):
                # when c_num is before num in lst, move c_num after num
                if c_num in lst[:i]:
                    good = False
                    lst.remove(c_num)
                    lst.insert(i, c_num)
                    rerun = True
                    break  # Restart checking for the current num
            if rerun:
                break
    if good:
        return []
    return lst


wrongs = [check_and_reorder(rule_dict, l) for l in C]
# print(wrongs)
total = 0
for wrong in wrongs:
    if wrong != []:
        total += wrong[len(wrong) // 2]

# print(total)
