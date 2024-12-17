import sys
from rich import print
import time
from collections import deque

input_path = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

text = open(input_path).read().split("\n")
visited = []


# BFS solution
def bfs(r, c):
    # print("start bfs for", r, c)
    q = deque()
    val = text[r][c]
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    q.append((r, c))
    visited.append((r, c))
    area = 1
    pm = 0
    pm_visited = []
    while q:
        r, c = q.popleft()
        # print(r, c)
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if (
                0 <= nr < len(text)
                and 0 <= nc < len(text[0])
                and text[nr][nc] == val
                and (nr, nc) not in visited
            ):
                area += 1
                q.append((nr, nc))
                visited.append((nr, nc))
            if (
                nr < 0
                or nc < 0
                or nr == len(text)
                or nc == len(text[0])
                or text[nr][nc] != val
            ):
                pm += 1
                pm_visited.append((nr, nc))
    # print(
    #     f"val: {val} area: {area}  pm: {pm}, len pm_visited: {len(pm_visited)}"
    return area * pm


total = 0
for i in range(len(text)):
    for j in range(len(text[0])):
        if (i, j) not in visited:
            total += bfs(i, j)

print(total)
