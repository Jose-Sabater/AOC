import re
import sys

input_path = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
with open(input_path) as f:
    text = f.read()
# remove new line characters
text.replace("\n", " ")

total = 0

# find first part before a don't()
pattern = r"(.*?)don't\(\)"
matches = re.findall(pattern, text)
first_match = matches[0]
print("First match")
print(first_match)
muls = re.findall(r"mul\(\d+,\d+\)", first_match)
# print(muls)
for mul in muls:
    m = re.findall(r"\d+", mul)
    total += int(m[0]) * int(m[1])
print("LEN FIRST MATCH")
print(len(first_match))
# find all instances of do() and the next mul() & don't() and the next mul
# middle part
# TODO there are do() dont before the first don't, so will need to remove those
text = text[len(first_match) : :]
pattern = r"do\(\)(.*?)don't\(\)"
middle_match = re.findall(pattern, text)
print("Middle")

for i, match in enumerate(middle_match):
    print(f"Match {i}")
    print(match)
    muls = re.findall(r"mul\(\d+,\d+\)", match)
    for mul in muls:
        m = re.findall(r"\d+", mul)
        total += int(m[0]) * int(m[1])


# final match
pattern = r"do\(\)"
# final_match = re.findall(pattern, text)[-1]
# print(re.finditer(pattern, text))
matches = re.finditer(pattern, text)
for match in matches:
    last_do_end = match.end()
last_match = text[last_do_end::]
print("Last match\n", last_match)
muls = re.findall(r"mul\(\d+,\d+\)", last_match)
for mul in muls:
    m = re.findall(r"\d+", mul)
    total += int(m[0]) * int(m[1])

print(total)
