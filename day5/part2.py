with open('input.txt', 'r') as file:
    content = file.read().strip()
    sections = content.split('\n\n')
    ranges = sections[0].splitlines()
    ingredients_id = sections[1].splitlines()

def parse_range(range_str):
    start, end = map(int, range_str.split('-'))
    return start, end

def merge_ranges(ranges):
    parsed_ranges = [parse_range(r) for r in ranges]
    parsed_ranges.sort()

    merged = []
    current_start, current_end = parsed_ranges[0]

    for start, end in parsed_ranges[1:]:
        if start <= current_end + 1:
            current_end = max(current_end, end)
        else:
            merged.append((current_start, current_end))
            current_start, current_end = start, end

    merged.append((current_start, current_end))
    return merged

print(merge_ranges(ranges))

counter_of_covered_ids = 0
merged_ranges = merge_ranges(ranges)
for start, end in merged_ranges:
    counter_of_covered_ids += (end - start + 1)

print(counter_of_covered_ids)