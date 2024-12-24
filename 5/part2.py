from itertools import combinations

with open('input.txt', 'r') as file:
    data = file.readlines()

ind = data.index('\n')
rules = data[:ind]
rules = [x.strip().split('|') for x in rules]
updates = data[ind+1:]
updates = [x.strip().split(',') for x in updates]

