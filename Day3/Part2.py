parts = [{}, {}, {}]


def itor(i: str):
    r = i.split(':')
    return range(int(r[0]), int(r[1])+1)


def get_numbers(line: str):
    start = 0
    value = ''
    for i, char in enumerate(line):
        if char.isdigit():
            if value == '':
                start = i
            value += char
        elif len(value) > 0:
            parts[2][str(start)+':'+str(start+len(value)-1)] = int(value)
            value = ''

    if len(value) > 0:
        parts[2][str(start)+':'+str(len(line)-1)] = int(value)


def get_adjacent_numbers(index):
    # Assuming index is for line containing numbers[1]
    adjacent_numbers = []
    adjacent_indices = [index - 1, index, index + 1]
    # Search 0/2
    for i in [0, 2]:
        for coords in parts[i]:
            for r in itor(coords):
                if r in adjacent_indices:
                    adjacent_numbers.append(parts[i][coords])
                    break
    # Search 1
    for coords in parts[1]:
        start, end = [int(c) for c in coords.split(':')]
        if end == index - 1 or start == index + 1:
            adjacent_numbers.append(parts[1][coords])
    
    return adjacent_numbers


def get_gears(line):
    gear_total = 0

    for i, x in enumerate(line):
        if x == '*':
            adjacent_numbers = get_adjacent_numbers(i)

            if len(adjacent_numbers) != 2:
                continue
            gear_total += adjacent_numbers[0] * adjacent_numbers[1]
    return gear_total


total = 0
with open('input.txt') as file:
    prev_line = ''
    for line in file:
        line = line.strip()
        
        parts = parts[1:]
        parts.append({})
        get_numbers(line)
        total += get_gears(prev_line)
        prev_line = line
    parts = parts[1:]
    parts.append({})
    total += get_gears(prev_line)
print(total)
