# Read input.txt
with open('input.txt', 'r') as file:
    lines = file.readlines()

counter = 50
null_times = 0
for line in lines:
    rotation, distance = line[:1], int(line[1:].strip())
    print(f"Rotation: {rotation}, Distance: {distance}")

    if rotation == 'R':
        counter += distance
    elif rotation == 'L':
        counter -= distance

    # Modulo to keep counter within 0-99 range
    counter %= 100
    print(f"Updated Counter: {counter}")
    if counter == 0:
        null_times += 1

print(f"Counter reached zero {null_times} times.")        
print(f"Final Counter Value: {counter}")