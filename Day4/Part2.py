num_cards = {}
total_cards = 0

with open('input.txt') as file:
    for line in file:
        total_cards += 1
        line = line.strip().split(': ')
        card_number = int(line[0].split(' ')[-1])
        if card_number not in num_cards:
            num_cards[card_number] = 1
        else:
            num_cards[card_number] += 1
        
        winning, numbers = line[1].split(' | ')
        winning = [x for x in filter(lambda x: len(x) > 0, winning.split(' '))]
        numbers = [x for x in filter(lambda x: len(x) > 0, numbers.split(' '))]

        matches = 0
        for number in numbers:
            if number in winning:
                matches += 1
        for i in range(matches):
            if card_number + i+1 in num_cards:
                num_cards[card_number + i+1] += num_cards[card_number]
            else:
                num_cards[card_number + i+1] = num_cards[card_number]

total = 0

for card in num_cards:
    if card <= total_cards:
        total += num_cards[card]
print(total)