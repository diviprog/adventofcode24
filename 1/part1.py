with open('input.txt', 'r') as file:
    data = file.readlines()

left = []
right = []
for line in data:
    left_num, right_num = line.split()
    left.append(int(left_num))
    right.append(int(right_num))

left.sort()
right.sort()
total = 0
for i in range(len(left)):
    total += abs(left[i] - right[i])

print(total)