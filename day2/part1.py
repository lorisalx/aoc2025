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
        if len(str(number)) % 2 == 0:
            str_num = str(number)
            half_len = len(str_num) // 2
            first_half = str_num[:half_len]
            second_half = str_num[half_len:]

            if first_half == second_half:
                counter += number
    
print(counter)