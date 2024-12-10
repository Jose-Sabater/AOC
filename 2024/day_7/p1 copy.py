from itertools import combinations

result = 292
operators = [11, 6, 16, 20]

simbols = "*+"
size = 3
simbols_comb = simbols
for i in range(size - 1):
    simbols_comb += "*+"
print(simbols_comb)
combs = combinations(simbols_comb, size)
u_c = list(set([comb for comb in combs]))
print(u_c)


def run_operation(sign, nums):
    print(f"runing operation for: {sign}, {nums}")
    if sign == "+":
        return sum(nums)
    if sign == "*":
        return nums[0] * nums[1]


for comb in u_c:
    print(f"starting combination: {comb}")
    r = 0
    for i, sign in enumerate(comb):
        if i == 0:
            r = run_operation(sign, operators[i : i + 2])
        else:
            r = run_operation(sign, [r, operators[i + 1]])
        # print(f"r is equal to{r}")
    if r == result:
        print("SUCCESS!!!!")
