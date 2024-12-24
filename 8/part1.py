from itertools import combinations

with open('input.txt', 'r') as file:
    map = file.readlines()

map = [x.strip() for x in map]

symbols = {}
for i in range(len(map)):
    for j in range(len(map[0])):
        if map[i][j] != '.':
            if map[i][j] in symbols:
                symbols[map[i][j]].append((i, j))
            else:
                symbols[map[i][j]] = [(i, j)]

antinodes = set()
for symbol in symbols:
    symbol_nodes = symbols[symbol]
    
    for pair in combinations(symbol_nodes, 2):
        x1, y1 = pair[0]
        x2, y2 = pair[1]
        
        dx = x2 - x1
        dy = y2 - y1
        
        antinode_diag1 = (x1 - dx, y1 - dy)
        antinode_diag2 = (x2 + dx, y2 + dy)
        
        if 0 <= antinode_diag1[0] < len(map) and 0 <= antinode_diag1[1] < len(map[0]):
            antinodes.add(antinode_diag1)
        if 0 <= antinode_diag2[0] < len(map) and 0 <= antinode_diag2[1] < len(map[0]):
            antinodes.add(antinode_diag2)

print(len(antinodes))