# Read input.txt
with open('input.txt', 'r') as file:
    lines = file.readlines()

counter = 50
click_times = 0
for line in lines:
    rotation, distance = line[:1], int(line[1:].strip())
    print(f"Rotation: {rotation}, Distance: {distance}")
    for _ in range(distance):
        if rotation == 'R':
            counter += 1
        elif rotation == 'L':
            counter -= 1
        if counter % 100 == 0:
            click_times += 1

print(f"Counter clicked {click_times} times.")
print(f"Final Counter Value: {counter}")