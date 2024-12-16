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
            if M[i][j] in hmap:
                for r, c in hmap[M[i][j]]:
                    # diff_r = i - r
                    # diff_c = j - c
                    # r - diff_r ==> r - i + r
                    # c - diff_c ==> c - j +  c
                    # i + diff_r ==> i + i - r
                    # j + diff_c ==> j + j - c
                    if 0 <= 2 * r - i < max_r and 0 <= 2 * c - j < max_c:
                        ret.append((2 * r - i, 2 * c - j))
                    if 0 <= 2 * i - r < max_r and 0 <= 2 * j - c < max_c:
                        ret.append((2 * i - r, 2 * j - c))
                hmap[M[i][j]].append([i, j])
            else:
                hmap.setdefault(M[i][j], []).append([i, j])


# print(ret)
# print(len(ret))
# print(set(ret))
print(len(list(set(ret))))
