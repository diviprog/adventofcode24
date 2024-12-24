with open('input.txt', 'r') as file:
    map = file.readlines()

map = [x.strip() for x in map]
rows, cols = len(map), len(map[0])

def bfs_trailhead(trailhead):
    queue_trail = [(trailhead, 0)]  # Position and current height
    visited = set()
    score = 0

    while queue_trail:
        position, height = queue_trail.pop(0)
        x, y = position

        # If height is 9, this trail is complete
        if height == 9:
            score += 1
            continue

        # Explore neighbors
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and (nx, ny) not in visited:
                if int(map[nx][ny]) == height + 1:
                    visited.add((nx, ny))
                    queue_trail.append(((nx, ny), height + 1))

    return score

# Find all trailheads (positions with height 0)
trailheads = [(i, j) for i in range(rows) for j in range(cols) if map[i][j] == '0']

# Calculate scores for all trailheads
total_score = sum(bfs_trailhead(trailhead) for trailhead in trailheads)
print(total_score)