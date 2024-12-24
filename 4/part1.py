with open('input.txt', 'r') as file:
    data = file.readlines()

data = list(map(lambda x: x.strip(), data))

count = 0
for i in range(len(data)):
    for j in range(len(data)):
        if data[i][j] == 'X':
            # down
            if (i-1>=0 and data[i-1][j] == 'M') and (i-2>=0 and data[i-2][j] == 'A') and (i-3>=0 and data[i-3][j] == 'S'):
                count += 1
            
            # up
            if (i+1 < len(data) and data[i+1][j] == 'M') and (i+2 < len(data) and data[i+2][j] == 'A') and (i+3 < len(data) and data[i+3][j] == 'S'):
                count += 1

            # right
            if (j+1 < len(data[i]) and data[i][j+1] == 'M') and (j+2 < len(data[i]) and data[i][j+2] == 'A') and (j+3 < len(data[i]) and data[i][j+3] == 'S'):
                count += 1

            # left
            if (j-1 >= 0 and data[i][j-1] == 'M') and (j-2 >= 0 and data[i][j-2] == 'A') and (j-3 >= 0 and data[i][j-3] == 'S'):
                count += 1

            # down-right
            if (i+1 < len(data) and j+1 < len(data[i]) and data[i+1][j+1] == 'M') and (i+2 < len(data) and j+2 < len(data[i]) and data[i+2][j+2] == 'A') and (i+3 < len(data) and j+3 < len(data[i]) and data[i+3][j+3] == 'S'):
                count += 1
            
            # down-left
            if (i+1 < len(data) and j-1 >= 0 and data[i+1][j-1] == 'M') and (i+2 < len(data) and j-2 >= 0 and data[i+2][j-2] == 'A') and (i+3 < len(data) and j-3 >= 0 and data[i+3][j-3] == 'S'):
                count += 1
            
            # up-right
            if (i-1 >= 0 and j+1 < len(data[i]) and data[i-1][j+1] == 'M') and (i-2 >= 0 and j+2 < len(data[i]) and data[i-2][j+2] == 'A') and (i-3 >=0 and j+3 < len(data[i]) and data[i-3][j+3] == 'S'):
                count += 1

            # up-left
            if (i-1 >= 0 and j-1 >= 0 and data[i-1][j-1] == 'M') and (i-2 >= 0 and j-2 >= 0 and data[i-2][j-2] == 'A') and (i-3 >=0 and j-3 >= 0 and data[i-3][j-3] == 'S'):
                count += 1

print(count)