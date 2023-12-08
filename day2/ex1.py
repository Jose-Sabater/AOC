import re
import numpy as np

with open("./day2/ex2.txt", "r") as file:
    lines = file.read()


red = 12
green = 13
blue = 14


# part 1
def get_possible_games(line):
    red = 12
    green = 13
    blue = 14
    game_id = line.split(":")[0].split("Game ")[1]
    lst = re.split("[;,]", line.split(":")[1])
    for el in lst:
        if "red" in el:
            if int(re.findall(r"\d+", el)[0]) > red:
                return 0
            # red -= int(re.findall(r"\d+", el)[0])
            # print(f"el is: {el} and found {n}")
        if "green" in el:
            if int(re.findall(r"\d+", el)[0]) > green:
                return 0
        if "blue" in el:
            if int(re.findall(r"\d+", el)[0]) > blue:
                return 0

    return int(game_id)


def min_cubes(line):
    lst = re.split("[;,]", line.split(":")[1])
    red = 0
    blue = 0
    green = 0
    for el in lst:
        if "red" in el:
            new_red = int(re.findall(r"\d+", el)[0])
            if new_red > red:
                red = new_red
        if "green" in el:
            new_green = int(re.findall(r"\d+", el)[0])
            if new_green > green:
                green = new_green
        if "blue" in el:
            new_blue = int(re.findall(r"\d+", el)[0])
            if new_blue > blue:
                blue = new_blue

    return red * green * blue


if __name__ == "__main__":
    total_part_1 = 0
    total_part_2 = 0
    for line in lines.split("\n"):
        total_part_1 += get_possible_games(line)
        total_part_2 += min_cubes(line)
    print("result part 1:", total_part_1)
    print("result part 2:", total_part_2)


# test = "Game 91: 9 red, 12 green, 1 blue; 11 green, 9 red, 2 blue; 1 blue, 8 red, 4 green; 6 red, 9 green; 2 blue, 10 red, 1 green; 2 blue, 15 green, 13 red"
# print(parse_line(test))
