# Read input.txt
with open('input.txt', 'r') as file:
    
    content = file.read().strip()
    sections = content.split('\n\n')
    ranges = sections[0].splitlines()
    ingredients_id = sections[1].splitlines()

def parse_range(range_str):
    start, end = map(int, range_str.split('-'))
    return start, end

def is_valid_ingredient(ingredient, ranges):
    for range_str in ranges:
        start, end = parse_range(range_str)
        if start <= ingredient <= end:
            return True
    return False

valid_ingredients_counter = 0

for ingredient_line in ingredients_id:
    ingredient = int(ingredient_line.strip())
    if is_valid_ingredient(ingredient, ranges):
        valid_ingredients_counter += 1

print(valid_ingredients_counter)