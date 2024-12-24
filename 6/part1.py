# Read the input
with open('input.txt', 'r') as file:
    grid = [list(line.strip()) for line in file.readlines()]

# Find the starting position
for y in range(len(grid)):
    for x in range(len(grid[0])):
        if grid[y][x] == '^':
            guard_y, guard_x = y, x
            break

# Track visited positions (including start position)
visited = {(guard_x, guard_y)}

# Direction mappings
directions = {
    '^': (0, -1),  # up: no change in x, decrease y
    '>': (1, 0),   # right: increase x, no change in y
    'v': (0, 1),   # down: no change in x, increase y
    '<': (-1, 0)   # left: decrease x, no change in y
}

# Next direction when turning right
turn_right = {'^': '>', '>': 'v', 'v': '<', '<': '^'}

# Current direction
current_dir = '^'

# Simulate guard movement
while True:
    # Get movement vector for current direction
    dx, dy = directions[current_dir]
    next_x, next_y = guard_x + dx, guard_y + dy
    
    # Check if guard would leave the grid
    if not (0 <= next_y < len(grid) and 0 <= next_x < len(grid[0])):
        break
        
    # Check if there's an obstacle ahead
    if grid[next_y][next_x] == '#':
        # Turn right
        current_dir = turn_right[current_dir]
    else:
        # Move forward
        grid[guard_y][guard_x] = 'X'  # Mark current position as visited
        guard_x, guard_y = next_x, next_y
        visited.add((guard_x, guard_y))
        
# Mark the final position
grid[guard_y][guard_x] = 'X'

# Print the final grid (for visualization)
for row in grid:
    print(''.join(row))

print(f"Number of distinct positions visited: {len(visited)}")