# Read input.txt
with open('input.txt', 'r') as file:
    lines = file.readlines()

counter = 0
for line in lines:
    current_num = 0
    for i in range(0, len(line) - 1):
        for j in range(i + 1, len(line)):
            num = int(line[i] + line[j])
            if num > current_num:
                current_num = num
    print(f"Processing line: {line.strip()} - Max two-digit number: {current_num}")
    counter += current_num
print(counter)