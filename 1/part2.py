from collections import Counter

with open('input.txt', 'r') as file:
    data = file.readlines()

left = []
right = []
for line in data:
    left_num, right_num = line.split()
    left.append(left_num)
    right.append(right_num)

right_freq = Counter(right)
total = 0
for left_num in left:
    if right_freq[left_num]:
        total += right_freq[left_num]*int(left_num)

print(total)