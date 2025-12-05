# Read input.txt
with open('input.txt', 'r') as file:
    lines = file.readlines()

def find_max_number(line, num_digits=12):
    n = len(line.strip())
    result = []
    start = 0

    for remaining in range(num_digits, 0, -1):
        end = n - remaining

        best_pos = start
        for pos in range(start, end + 1):
            if line[pos] > line[best_pos]:
                best_pos = pos

        result.append(line[best_pos])
        start = best_pos + 1

    return int(''.join(result))


counter = 0
for line in lines:
    current_num = find_max_number(line.strip(), 12)
    counter += current_num
print(counter)