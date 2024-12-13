import sys
from rich import print
from collections import deque


input_path = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
with open(input_path) as f:
    text = f.read().splitlines()

M = []
for line in text:
    M.append(
        [int(num) if num.isalnum() else 50 for num in line]
    )  # to accomodate for tests


def bfs(r, c):
    visited_9s = list()  # set()
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    val = 0  # starting value
    q = deque()
    q.append((r, c))
    while q:
        r, c = q.popleft()
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < len(M) and 0 <= nc < len(M[0]) and M[nr][nc] - M[r][c] == 1:
                q.append((nr, nc))

            if (
                0 <= nr < len(M)
                and 0 <= nc < len(M[0])
                and M[nr][nc] - M[r][c] == 1
                and M[r][c] == 8
                and M[nr][nc] not in visited_9s
            ):
                visited_9s.append((nr, nc))

    return visited_9s


total = 0
for r in range(len(M)):
    for c in range(len(M[0])):
        if M[r][c] == 0:

            res = bfs(r, c)
            # print(res)
            total += len(res)


print(total)
