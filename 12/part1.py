from collections import defaultdict

with open('input.txt', 'r') as file:
    map = file.readlines()

map = [x.strip() for x in map]

visited = set()
regions = defaultdict(list)
rows = len(map)
cols = len(map[0])
def flood_fill(r, c, plant_type):
        if (r, c) in visited or r < 0 or r >= rows or c < 0 or c >= cols or map[r][c] != plant_type:
            return 0, set()
            
        visited.add((r, c))
        points = {(r, c)}
        
        for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
            area, new_points = flood_fill(r + dr, c + dc, plant_type)
            points.update(new_points)
            
        return len(points), points

def get_perimeter(points):
    perimeter = 0
    for r, c in points:
        for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
            if (r + dr, c + dc) not in points:
                perimeter += 1
    return perimeter

for r in range(rows):
    for c in range(cols):
        if (r, c) not in visited:
            plant_type = map[r][c]
            area, points = flood_fill(r, c, plant_type)
            if area > 0:
                perimeter = get_perimeter(points)
                regions[plant_type].append((area, perimeter))

total_price = 0
for plant_type, region_list in regions.items():
    for area, perimeter in region_list:
        price = area * perimeter
        total_price += price

print(total_price)