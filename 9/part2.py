from collections import Counter

with open('input.txt', 'r') as file:
    data = file.read()

data = list(data)
data = [int(x) for x in data]

disk = list()
for i in range(len(data)):
    for j in range(data[i]):
        if i % 2 == 0:
            disk.append(i//2)
        else:
            disk.append('.')



checksum = 0
for i in range(len(disk)):
    if disk[i] != '.':
        checksum += i*disk[i]

print(checksum)