def compute_array(target, array):
    if len(array) == 0:
        return target == 0
    if len(array) == 1:
        return array[0] == target

    if compute_array(target, [array[0] + array[1]] + array[2:]) or compute_array(target, [array[0] * array[1]] + array[2:]) or compute_array(target, [array[0]*10**len(str(array[1]))+array[1]]+array[2:]):
        return True
    
    return False

with open('input.txt', 'r') as file:
    data = file.readlines()

total = 0
for line in data:
    values = line.strip().split()
    target = int(values[0][:-1])
    array = [int(x) for x in values[1:]]
    
    if compute_array(target, array):
        total += target

print(total)