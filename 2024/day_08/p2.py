import sys
from rich import print


input_path = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
with open(input_path) as f:
    text = f.read()

M = text.splitlines()

max_c = len(M[0])
max_r = len(M)
ret = []
hmap = {}
for i in range(len(M)):
    for j in range(len(M[0])):
        if M[i][j].isalnum():
            ret.append((i, j))  # add all nodes
            if M[i][j] in hmap:
                for r, c in hmap[M[i][j]]:
                    for n in range(
                        1, max_c
                    ):  # this is the maximum possible additions if it went 1 by 1
                        diff_r = i - r
                        diff_c = j - c
                        # r - diff_r
                        # c - diff_c
                        # i + diff_r
                        # j + diff_c
                        if 0 <= r - diff_r * n < max_r and 0 <= c - diff_c * n < max_c:
                            ret.append((r - diff_r * n, c - diff_c * n))
                        if 0 <= i + diff_r * n < max_r and 0 <= j + diff_c * n < max_c:
                            ret.append((i + diff_r * n, j + diff_c * n))
                hmap[M[i][j]].append([i, j])
            else:
                hmap.setdefault(M[i][j], []).append([i, j])


# print(ret)
# print(len(ret))
# print(set(ret))
print(len(list(set(ret))))
