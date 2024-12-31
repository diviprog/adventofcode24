def parse_input(lines):
    lines = [line.strip() for line in lines]

    positions = []
    velocities = []
    for line in lines:
        pos_str, vel_str = line.split(' ')
        position = tuple(map(int, pos_str.split('=')[1].split(',')))
        velocity = tuple(map(int, vel_str.split('=')[1].split(',')))
        positions.append(position)
        velocities.append(velocity)
    return positions, velocities

with open('input.txt', 'r') as file:
    lines = file.readlines()

positions, velocities = parse_input(lines)

num_iters = 100
rows = 103
cols = 101

for iter in range(num_iters):
    for i in range(len(positions)):
        pos_x, pos_y = positions[i]
        v_x, v_y = velocities[i]
        pos_x += v_x
        pos_y += v_y
        pos_x %= cols
        pos_y %= rows
        positions[i] = (pos_x, pos_y)
    
quads = [0,0,0,0]
for pos_x, pos_y in positions:
    if pos_x < 50 and pos_y < 51:
        quads[0] += 1
    elif pos_x > 50 and pos_y < 51:
        quads[1] += 1
    elif pos_x < 50 and pos_y > 51:
        quads[2] += 1
    elif pos_x > 50 and pos_y > 51:
        quads[3] += 1

print(quads[0]*quads[1]*quads[2]*quads[3])