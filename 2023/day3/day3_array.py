import numpy as np
import re


with open("./day3/day3.txt", "r") as f:
    lines = f.read()

special = []
for line in lines.split("\n"):
    special.extend(re.findall(r"[^\w\s.]", line))
symbols = list(set(special))

array = np.array([list(line) for line in lines.split("\n")])

symbols_pos = []
for i in range(array.shape[0]):
    for j in range(array.shape[1]):
        if array[i, j] in symbols:
            symbols_pos.append([i, j])

pos = symbols_pos[0]
print(pos)
print(array[pos[0], pos[1]])

top_left = [-1,-1]
top_center = [0, -1]
top_right = [1,-1]
center_left = [-1,0]
center_right = [1,0]
bottom_left = [-1,1]
bottom_center = [0,1]
bottom_right = [1,1]

neighbors = [top_left, top_center, top_right, center_left, center_right, bottom_left, bottom_center, bottom_right]

for i in range(array.shape[0]):
    for j in range(array.shape[1]):
        for neighbor in neighbors:
            if array[i,j] 

#unfinished


foo = [1, 2]
bar = [1, 2]
print(foo + bar)
