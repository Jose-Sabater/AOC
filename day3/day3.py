import re

with open("./day3/day3.txt", "r") as f:
    # with open("./day3/test.txt", "r") as f:
    lines = f.read()

special = []
for line in lines.split("\n"):
    special.extend(re.findall(r"[^\w\s.]", line))
symbols = list(set(special))
print(symbols)

array = [[el for el in line] for line in lines.split("\n")]
valid_n_pos = []
nrs = 0
nr_dict = {}
for r in range(len(array)):
    # print(array[r])
    for c in range(len(array[r])):
        if array[r][c].isdigit():
            # Logic for iterating neighbors
            for i in [-1, 0, 1]:
                rr = r + i
                for j in [-1, 0, 1]:
                    cc = c + j
                    if rr > 0 and cc > 0 and rr < len(array) and cc < len(array[r]):
                        # print(r, c, rr, cc)
                        # Find neighbor symbols
                        _nr = ""
                        neg = False
                        if array[rr][cc] in symbols:
                            valid_n_pos.append([r, c])
                            _nr = array[r][c]
                            # check ahead until nr ends
                            for next in range(c + 1, len(array) - 1):
                                if array[r][next].isdigit():
                                    _nr += array[r][next]
                                else:
                                    fd_pos = [r, next]  # final digit position
                                    break
                            # check earlier where nr starts
                            for previous in range(c - 1, -2, -1):
                                if array[r][previous].isdigit():
                                    _nr = array[r][previous] + _nr
                                if array[r][previous] == "-":
                                    neg = True
                                if previous < 0 or not array[r][previous].isdigit():
                                    first_d_pos = [r, previous]
                                    break

                            nr_dict[f"{r,first_d_pos,fd_pos}"] = int(_nr) 
                            if neg:# Not sure about this , if such maybe then the negative doesnt count as symbol
                                nr_dict[f"{r,first_d_pos,fd_pos}"] = -int(_nr)


#TODO  negative numbers?
print(nr_dict.values())
ans = 0
for k, v in nr_dict.items():
    ans += v

print(ans)
