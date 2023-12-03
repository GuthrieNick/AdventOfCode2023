powers = 0

with open('input.txt') as file:
    for game in file:
        parts = game[:-1].split(": ")
        rounds = [cubes.split(', ') for cubes in parts[1].split('; ')] # [['3 blue', '2 green', '6 red'], ['17 green', '4 red', '8 blue'], ...]
        mins = {
            'red': 0,
            'blue': 0,
            'green': 0
        }
        for round in rounds:
            for color in round:
                color = color.split(' ')
                if int(color[0]) > mins[color[1]]:
                    mins[color[1]] = int(color[0])
        powers += mins['red'] * mins['blue'] * mins['green']
    print(powers)
        