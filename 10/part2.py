with open('input.txt', 'r') as file:
    map = file.readlines()

map = [x.strip() for x in map]

queue_trailheads = []
for i in range(len(map)):
    for j in range(len(map[0])):
        if map[i][j] == '0':
            queue_trailheads.append((i,j))

queue_trail = []
count = 0
while len(queue_trailheads) != 0:
    head = queue_trailheads.pop(0)
    queue_trail.append((head, 0))
    while len(queue_trail) != 0:
        position, height = queue_trail.pop(0)
        if height == 9:
            count += 1
            continue
        position_x, position_y = position[0], position[1]
        if position_x < len(map)-1 and int(map[position_x+1][position_y]) == height+1:
            queue_trail.append(((position_x+1, position_y), height+1))
        if 1 <= position_x and int(map[position_x-1][position_y]) == height+1:
            queue_trail.append(((position_x-1, position_y), height+1))
        if position_y < len(map[0])-1 and int(map[position_x][position_y+1]) == height+1:
            queue_trail.append(((position_x, position_y+1), height+1))
        if 1 <= position_y and int(map[position_x][position_y-1]) == height+1:
            queue_trail.append(((position_x, position_y-1), height+1))

print(count)