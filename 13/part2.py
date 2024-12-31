import re
from scipy.optimize import linprog

def parse_input(input_lines):
    button_a_coordinates = []
    button_b_coordinates = []
    prize_coordinates = []

    for line in input_lines:
        line = line.strip()
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
    A_eq = [[button_a[0], button_b[0]], [button_a[1], button_b[1]]]
    b_eq = [prize[0], prize[1]]
    bounds = [(0, None), (0, None)]

    result = linprog(c=[3, 1], A_eq=A_eq, b_eq=b_eq, bounds=bounds, method='highs')

    if result.success and result.x is not None:
        a, b = result.x
        if a.is_integer() and b.is_integer():
            return int(3 * a + b)
    return 0

with open("input.txt", "r") as file:
    lines = file.readlines()
lines = [x.strip() for x in lines]

button_a_coords, button_b_coords, prize_coords = parse_input(lines)
prize_coords = [(x + 10**13, y + 10**13) for x, y in prize_coords]

total_cost = 0
for i in range(len(button_a_coords)):
    cost = min_cost(button_a_coords[i], button_b_coords[i], prize_coords[i])
    total_cost += cost

print(f"Total cost: {total_cost}")