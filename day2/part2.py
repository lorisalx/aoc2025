# Read input.txt
with open('input.txt', 'r') as file:
    file_content = file.read()

ranges = file_content.split(",")

counter = 0
for rang in ranges:
    rang = rang.split("-")
    start = int(rang[0])
    end = int(rang[1])
    print(f"Processing range: {start} to {end}")
    for number in range(start, end + 1):
        for i in range(1, (len(str(number)) // 2) + 1):
            str_num = str(number)
            parts = [str_num[j:j+i] for j in range(0, len(str_num), i)]
            if all(part == parts[0] for part in parts):
                counter += number
                break
            
    
print(counter)