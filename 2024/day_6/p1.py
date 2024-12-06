import sys
import re

input_path = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
with open(input_path) as f:
    text = f.read()


class LabRoom:
    def __init__(self, M: list[str], r: int, c: int):
        self.r = r
        self.c = c
        self.M = M
        self.visited = set([(self.r, self.c)])
        self.directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # up, right, down, left
        self.current_direction = 0  # Start by moving up

    def _print_current(self, direction):
        print(f"current position: ({self.r}, {self.c})")
        print(f"trying to move: {direction}")

    def _is_valid_move(self, r, c):
        return 0 <= r < len(self.M) and 0 <= c < len(self.M[0]) and self.M[r][c] == "."

    def _get_total_visited(self):
        return len(self.visited)

    def run(self):
        while True:
            # next position
            dr, dc = self.directions[self.current_direction]
            # will it leave the board
            if not 0 <= self.r + dr < len(self.M) and 0 <= self.c + dc < len(self.M[0]):
                break
            new_r, new_c = self.r + dr, self.c + dc

            if self._is_valid_move(new_r, new_c):
                # next pos
                self.r, self.c = new_r, new_c
                self.visited.add((self.r, self.c))
            else:
                # change direction (turn right)
                self.current_direction = (self.current_direction + 1) % 4

            self._print_current(["up", "right", "down", "left"][self.current_direction])

            # if we cannot move in any direction, stop
            all_directions_checked = all(
                not self._is_valid_move(self.r + dr, self.c + dc)
                for dr, dc in self.directions
            )
            if all_directions_checked:
                break

        return self._get_total_visited()


# pattern = r"\^"
# print(text.find("^"))
M = [line for line in text.split("\n")]

print(M)
print(M[0][0])
for i in range(len(M)):
    for j in range(len(M[0])):
        if M[i][j] == "^":
            x, y = i, j
            M[i] = M[i].replace("^", ".")
print(M)

print(x, y)
print(len(M) - 1)
lr = LabRoom(M, x, y)
print(lr.run())
# Go up
# Go right
# Go down
# Go left
