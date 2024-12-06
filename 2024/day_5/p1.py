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


wrong = []
for i, row in enumerate(C):
    for j, value in enumerate(row):
        if value in rule_dict:
            # if it appears earlier in the row
            if any(num in row[:j] for num in rule_dict[value]):
                # print(row)
                wrong.append(i)
                break
# print(wrong)
total = 0
for idx, row in enumerate(C):
    if idx not in wrong:
        total += row[len(row) // 2]

print("Total:", total)
