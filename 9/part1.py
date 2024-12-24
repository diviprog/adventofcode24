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

low_ind, high_ind = 0, len(disk)-1
while low_ind < high_ind:
    while disk[low_ind] == '.':
        if disk[high_ind] != '.':
            disk[low_ind] = disk[high_ind]
            disk[high_ind] = '.'
        else:
            high_ind -= 1
    low_ind += 1

checksum = 0
for i in range(len(disk)):
    if disk[i] == '.':
        break
    checksum += i*disk[i]

print(checksum)