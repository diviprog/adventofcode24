with open('input.txt', 'r') as file:
    data = file.read()

data = data.strip().split(' ')
stones = [int(x) for x in data]

num_iter = 75
previous_num = len(stones)
for i in range(num_iter):
    stones_to_add = []
    stone_ind = 0
    while stone_ind < len(stones):
        if stones[stone_ind] == 0:
            stones[stone_ind] = 1
        elif len(str(stones[stone_ind])) % 2 == 0:
            num = stones.pop(stone_ind)
            stone_ind -= 1
            len_num = len(str(num))
            num1 = num // (10**(len_num//2))
            num2 = num % (10**(len_num//2))
            stones_to_add.append(num1)
            stones_to_add.append(num2)
        else:
            stones[stone_ind] *= 2024
        stone_ind += 1
    stones.extend(stones_to_add)
    print(len(stones), len(stones)/previous_num, i)
    previous_num = len(stones)

print(len(stones))