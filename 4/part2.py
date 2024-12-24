with open('input.txt', 'r') as file:
    data = file.readlines()

data = list(map(lambda x: x.strip(), data))

count = 0
for i in range(len(data)):
    for j in range(len(data[i])):
        if data[i][j] == 'A':
            # Check for cross pattern (diagonals)
            if (
                i - 1 >= 0 and i + 1 < len(data) and
                j - 1 >= 0 and j + 1 < len(data[i]) and
                (
                    (data[i - 1][j - 1] == 'M' and data[i + 1][j + 1] == 'S') or
                    (data[i - 1][j - 1] == 'S' and data[i + 1][j + 1] == 'M')
                ) and
                (
                    (data[i - 1][j + 1] == 'S' and data[i + 1][j - 1] == 'M') or
                    (data[i - 1][j + 1] == 'M' and data[i + 1][j - 1] == 'S')
                )
            ):
                count += 1

print(count)