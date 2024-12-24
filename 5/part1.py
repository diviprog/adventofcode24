from itertools import combinations

with open('input.txt', 'r') as file:
    data = file.readlines()

ind = data.index('\n')
rules = data[:ind]
rules = [x.strip().split('|') for x in rules]
updates = data[ind+1:]
updates = [x.strip().split(',') for x in updates]

correct_updates = []
for update in updates:
    ordered_updates = list(combinations(update, 2))
    unordered_updates = [list(x[::-1]) for x in ordered_updates]
    flag = True
    for i in unordered_updates:
        if i in rules:
            flag = False
            break
    if flag:
        correct_updates.append(update)

total = 0
for update in correct_updates:
    total += int(update[len(update)//2])

print(total)