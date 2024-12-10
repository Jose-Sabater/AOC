import sys
from rich import print


input_path = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
with open(input_path) as f:
    text = f.read()

# print(text)
lst = []
spaces = 0
counter = 0
for i, num in enumerate(text):
    num = int(num)
    if i % 2 == 0:
        lst.extend([counter] * num)  
        counter += 1
    else:
        lst.extend([-counter] * num)

# print(lst)

for idx, num in enumerate(lst):
    if num < 0 :
        while lst[-1]<0:
            lst.pop(-1)
        lst[idx] = lst[-1]
        lst.pop(-1)

# print(lst)
total = 0
for idx, num in enumerate(lst):
    total += idx*num

print(total)