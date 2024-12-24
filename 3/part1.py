import re

with open('input.txt', 'r') as file:
    data = file.read()

pattern = r'mul\((\d{1,3}),(\d{1,3})\)'
    
matches = re.findall(pattern, data)
    
total = sum(int(x) * int(y) for x, y in matches)
    
print(total)