import sys
from rich import print


input_path = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
with open(input_path) as f:
    text = f.read()

# print(text)
lst = []
spaces = 0
counter = 0
for i, num in enumerate(text):
    num = int(num)
    if i % 2 == 0:
        lst.extend([counter] * num)
        counter += 1
    else:
        lst.extend([-counter] * num)

# part 2 strat
# create a copy of the original data, loop through it backwards
# When we loop, keep the nr, the size and the indexes of the group
# create a loop that iterates through the "real state list". It searches for space, increase by 1 for each iteration
# keeps track of the indexes of the current space
# doesnt go until the end, goes until the smallest index of our group
# if the space matches the size of the numbers replace


def search_n_replace(num, idxs):
    available_idxs = []
    for i in range(len(lst)):
        if available_idxs == [] and lst[i] < 0:  # first ocurrence
            available_num = lst[i]

        if i == min(idxs):  # stopping
            # print(f"No available space for num {num} and size {len(idxs)}")
            break

        if lst[i] < 0 and lst[i] == available_num:
            available_idxs.append(i)
            if len(idxs) == len(available_idxs):
                for av_idx in available_idxs:
                    lst[av_idx] = num
                    # print(lst)
                    available_idxs = []  # start over
                for idx in idxs:
                    lst[idx] = -num
                break

            if lst[i + 1] != available_num:  # checks for the next
                available_idxs = []


queue = lst.copy()

idxs = []
for i, q_n in enumerate(queue[::-1]):
    if q_n > 0 and idxs == []:  # first time
        num = q_n

    if q_n > 0 and q_n == num:
        idxs.append(len(queue) - 1 - i)

    if q_n != num and q_n > 0:
        # this searches for space
        search_n_replace(num, idxs)
        # replace the list with the new value
        num = q_n
        idxs = [len(queue) - 1 - i]

# print(lst)
total = 0
for idx, num in enumerate(lst):
    if num > 0:
        total += idx * num
print(total)
