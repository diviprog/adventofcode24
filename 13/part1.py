import re
import numpy as np

def parse_input(input_lines):
    button_a_coordinates = []
    button_b_coordinates = []
    prize_coordinates = []

    for line in input_lines:
        line = line.strip()  # Remove any trailing spaces or newlines
        button_a_match = re.match(r"Button A: X\+(\d+), Y\+(\d+)", line)
        button_b_match = re.match(r"Button B: X\+(\d+), Y\+(\d+)", line)
        prize_match = re.match(r"Prize: X=(\d+), Y=(\d+)", line)

        if button_a_match:
            x_offset, y_offset = map(int, button_a_match.groups())
            button_a_coordinates.append((x_offset, y_offset))
        elif button_b_match:
            x_offset, y_offset = map(int, button_b_match.groups())
            button_b_coordinates.append((x_offset, y_offset))
        elif prize_match:
            x_offset, y_offset = map(int, prize_match.groups())
            prize_coordinates.append((x_offset, y_offset))

    return button_a_coordinates, button_b_coordinates, prize_coordinates

def min_cost(button_a, button_b, prize):
    for a in range(101):
        for b in range(101):
            if a * button_a[0] + b * button_b[0] == prize[0] and \
               a * button_a[1] + b * button_b[1] == prize[1]:
                return 3 * a + b

    return 0

with open("input.txt", "r") as file:
    lines = file.readlines()

button_a_coords, button_b_coords, prize_coords = parse_input(lines)

total_cost = 0
for i in range(len(button_a_coords)):
    cost = min_cost(button_a_coords[i], button_b_coords[i], prize_coords[i])
    total_cost += cost

print(total_cost)