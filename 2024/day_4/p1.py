import sys

input_path = sys.argv[1] if len(sys.argv) > 1 else "input.txt"


with open(input_path) as f:
    text = f.read().splitlines()

counter = 0
# Horizontal
for row in range(len(text)):
    for col in range(len(text[0])-3):
        if text[row][col]=="X" and text[row][col+1] == "M" and text[row][col+2] == "A" and text[row][col+3] == "S":
            counter +=1
        if text[row][col]=="S" and text[row][col+1] == "A" and text[row][col+2] == "M" and text[row][col+3] == "X":
            counter +=1
# Vertical
for row in range(len(text)-3):
    for col in range(len(text[0])):
        if text[row][col] =="X" and text[row+1][col] == "M" and text[row+2][col] == "A" and text[row+3][col] == "S":
            counter +=1
        if text[row][col] =="S" and text[row+1][col] == "A" and text[row+2][col] == "M" and text[row+3][col] == "X":
            counter +=1

# Diagonal \
for row in range(len(text)-3):
    for col in range(len(text[0])-3):
        if text[row][col] =="X" and text[row+1][col+1] == "M" and text[row+2][col+2] == "A" and text[row+3][col+3] == "S": 
            counter +=1
        if text[row][col] =="S" and text[row+1][col+1] == "A" and text[row+2][col+2] == "M" and text[row+3][col+3] == "X":
            counter +=1

# #Diagonal /
for row in range(len(text)-3):
    for col in range(len(text[0])-3):
        if text[row][col+3] =="X" and text[row+1][col+2] == "M" and text[row+2][col+1] == "A" and text[row+3][col] == "S":
            counter +=1
        if text[row][col+3] =="S" and text[row+1][col+2] == "A" and text[row+2][col+1] == "M" and text[row+3][col] == "X":
            counter +=1

print(counter)