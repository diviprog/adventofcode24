import re

def sum_enabled_muls(input_string):
    # Regular expressions for parsing instructions
    mul_pattern = r"mul\((\d+),(\d+)\)"
    do_pattern = r"do\(\)"
    dont_pattern = r"don't\(\)"
    
    # Initialize variables
    is_enabled = True
    total_sum = 0
    
    # Tokenize the input
    tokens = re.findall(f"{mul_pattern}|{do_pattern}|{dont_pattern}", input_string)
    
    print(tokens)
    # Process each token
    for token in tokens:
        if token[0]:  # mul(a, b)
            a, b = int(token[0]), int(token[1])
            if is_enabled:
                total_sum += a * b
        elif token[2]:  # do()
            is_enabled = True
        elif token[3]:  # don't()
            is_enabled = False
    
    return total_sum

with open('input.txt', 'r') as file:
    input_data = file.read()
result = sum_enabled_muls(input_data)
print(result)