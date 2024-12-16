import sys

input_path = sys.argv[1] if len(sys.argv) > 1 else "input.txt"


with open(input_path) as f:
    text = f.read().splitlines()

counter = 0

#find A
for r in range(1, len(text)-1):
    for c in range(1, len(text[0])-1):
        if text[r][c]=="A":
            # 2 m on top
            if text[r-1][c-1] == "M" and text[r-1][c+1] == "M" and text[r+1][c-1] == "S" and text[r+1][c+1]== "S":
                counter +=1
            # 2 m on left
            if text[r-1][c-1] == "M" and text[r-1][c+1] == "S" and text[r+1][c-1] == "M" and text[r+1][c+1]== "S":
                counter +=1
            # 2 m on bottom
            if text[r-1][c-1] == "S" and text[r-1][c+1] == "S" and text[r+1][c-1] == "M" and text[r+1][c+1]== "M":
                counter +=1
            # 2 m on right
            if text[r-1][c-1] == "S" and text[r-1][c+1] == "M" and text[r+1][c-1] == "S" and text[r+1][c+1]== "M":
                counter +=1

print(counter)