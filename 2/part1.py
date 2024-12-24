def is_safe(report):
    for i in range(len(report) - 1):
        diff = report[i + 1] - report[i]
        if abs(diff) < 1 or abs(diff) > 3:
            return False

    if all(report[i] < report[i + 1] for i in range(len(report) - 1)) or \
       all(report[i] > report[i + 1] for i in range(len(report) - 1)):
        return True

    return False

with open('input.txt', 'r') as file:
    reports = [list(map(int, line.strip().split())) for line in file]

safe_count = sum(1 for report in reports if is_safe(report))

print(safe_count)