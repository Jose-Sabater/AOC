import sys

input_path = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
with open(input_path) as f:
    text = f.read()

nr = 50
counter = 0
for line in text.strip().split("\n"):
    direction = line[0]
    amount = int(line[1:])
    if direction == "L":
        nr = (nr - amount) % 100
    else:
        nr = (nr + amount) % 100
    if nr == 0:
        counter += 1
print(counter)
        
    