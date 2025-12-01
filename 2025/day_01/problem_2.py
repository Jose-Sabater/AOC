import sys

input_path = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
with open(input_path) as f:
    text = f.read()

nr = 50
counter = 0
for line in text.strip().split("\n"):
    direction = line[0]
    amount = int(line[1:])

    # Calculate clicks needed to first hit zero
    if direction == "L":
        first_zero = nr if nr > 0 else 100
    else:
        first_zero = 100 - nr

    # Count how many times we land on zero during this rotation
    if amount >= first_zero:
        counter += (amount - first_zero) // 100 + 1

    # Update position
    if direction == "L":
        nr = (nr - amount) % 100
    else:
        nr = (nr + amount) % 100

print(counter)
