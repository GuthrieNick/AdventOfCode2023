symbols = [[], [], []]

def get_symbols(line):
    for i in range(len(line)):
        if line[i] == '.' or line[i].isnumeric():
            continue
        symbols[2].append(i)


def symbol_adjacent(index, length):
    for i in range(index - length - 1, index+1):
        if i in symbols[0] or i in symbols[1] or i in symbols[2]:
            return True
    return False

def get_line_total(line):
    line_total = 0
    current_part = ''

    for i in range(len(line)):
        if line[i].isnumeric():
            current_part += line[i]
        
        elif len(current_part) > 0:
            if symbol_adjacent(i, len(current_part)):
                line_total += int(current_part)
            
            current_part = ''
    
    if len(current_part) > 0 and symbol_adjacent(len(line), len(current_part)):
        line_total += int(current_part)
    return line_total

previous_line = ''
total = 0

with open('input.txt') as file:
    for line in file:
        line = line.strip()
        # Shift symbols
        symbols = symbols[1:]
        symbols.append([])
        get_symbols(line)
        # parse previous line for parts
        total += get_line_total(previous_line)
        previous_line = line # shift line
    # parse last line
    symbols = symbols[1:]
    symbols.append([])
    total += get_line_total(previous_line)

print(total)
