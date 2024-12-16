import re
import sys

input_path = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
with open(input_path) as f:
    text = f.read()

pattern = r"mul\(\d+,\d+\)"
matches = re.findall(pattern, text)

p2 = r"\d+"
# print(matches)
result = 0
for match in matches:
    nums = re.findall(p2, match)
    result += int(nums[0]) * int(nums[1])


print(result)
