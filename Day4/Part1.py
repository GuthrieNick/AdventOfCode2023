points = 0


with open('input.txt') as file:
    for line in file:
        winning, numbers = line.strip().split(':')[1].split(' | ')
        winning = [x for x in filter(lambda x: len(x) > 0, winning.split(' '))]
        numbers = [x for x in filter(lambda x: len(x) > 0, numbers.split(' '))]
        value = 0
        for number in numbers:
            if number in winning:
                if value == 0:
                    value = 1
                else:
                    value *= 2
        points += value
    print(points)