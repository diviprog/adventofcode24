from collections import defaultdict, deque
from typing import Set, Tuple, List, Dict, Set

def find_regions_by_sides(grid: List[str]) -> int:
    rows, cols = len(grid), len(grid[0])
    visited = set()
    regions = defaultdict(list)
    
    def get_sides(points: Set[Tuple[int, int]]) -> int:
        segments = set()
        for r, c in points:
            for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
                nr, nc = r + dr, c + dc
                if (nr, nc) not in points:
                    if dc == 0:
                        if dr == 1:
                            segments.add(((r+1, c), 'h'))
                        else:
                            segments.add(((r, c), 'h'))
                    else:
                        if dc == 1:
                            segments.add(((r, c+1), 'v'))
                        else:
                            segments.add(((r, c), 'v'))
        
        sides = 0
        remaining = segments.copy()
        
        while remaining:
            current = remaining.pop()
            sides += 1
            
            if current[1] == 'h':
                r, c = current[0]
                pos = r, c + 1
                while ((pos, 'h')) in remaining:
                    remaining.remove((pos, 'h'))
                    pos = (pos[0], pos[1] + 1)
                
                pos = r, c - 1
                while ((pos, 'h')) in remaining:
                    remaining.remove((pos, 'h'))
                    pos = (pos[0], pos[1] - 1)
                    
            else:
                r, c = current[0]
                pos = r + 1, c
                while ((pos, 'v')) in remaining:
                    remaining.remove((pos, 'v'))
                    pos = (pos[0] + 1, pos[1])
                
                pos = r - 1, c
                while ((pos, 'v')) in remaining:
                    remaining.remove((pos, 'v'))
                    pos = (pos[0] - 1, pos[1])
        
        return sides

    def flood_fill(r, c, plant_type):
        if (r, c) in visited or r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != plant_type:
            return 0, set()
            
        visited.add((r, c))
        points = {(r, c)}
        
        for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
            area, new_points = flood_fill(r + dr, c + dc, plant_type)
            points.update(new_points)
            
        return len(points), points

    for r in range(rows):
        for c in range(cols):
            if (r, c) not in visited:
                plant_type = grid[r][c]
                area, points = flood_fill(r, c, plant_type)
                if area > 0:
                    sides = get_sides(points)
                    regions[plant_type].append((area, sides))

    total_price = 0
    for plant_type, region_list in regions.items():
        for area, sides in region_list:
            price = area * sides
            total_price += price

    return total_price

with open('input.txt', 'r') as file:
    map = file.readlines()

map = [x.strip() for x in map]
print(find_regions_by_sides(map))