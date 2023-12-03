# Game 1: 3 blue, 2 green, 6 red; 17 green, 4 red, 8 blue; 2 red, 1 green, 10 blue; 1 blue, 5 green

TOTAL_COUNT = {
    'red': 12,
    'green': 13,
    'blue': 14
}

RED = 12
GREEN = 13
BLUE = 14

games = 0
with open('input.txt') as file:
    for game in file:
        parts = game[:-1].split(": ")
        gameNumber = int(parts[0].split(' ')[1])
        rounds = [cubes.split(', ') for cubes in parts[1].split('; ')] # [['3 blue', '2 green', '6 red'], ['17 green', '4 red', '8 blue'], ...]
        playable = True
        for round in rounds:
            for color in round:
                color = color.split(' ')
                if int(color[0]) > TOTAL_COUNT[color[1]]:
                    playable = False
                    break
                if not playable:
                    break
        if playable:
            games += gameNumber
    print(games)