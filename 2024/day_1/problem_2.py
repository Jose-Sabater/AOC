import sys

input_path = sys.argv[1] if len(sys.argv) > 1 else "input.txt"


def solve_problem(input_path: str) -> int:
    with open(input_path) as f:
        text = f.read().splitlines()

    lst_1 = [int(line.split("   ")[0]) for line in text]
    lst_2 = [int(line.split("   ")[1]) for line in text]
    result = []
    for num in lst_1:
        counter = 0
        for i in lst_2:
            if i == num:
                counter += 1
        result.append(num * counter)
    return sum(result)


print(solve_problem((input_path)))
