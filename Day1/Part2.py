from functools import reduce
writtenOut = ['one','two','three','four','five','six','seven','eight','nine']
replacer = ['o1e', 't2o', 't3e', 'f4r','f5e','s6x','s7n','e8t','n9e']
values = []
with open('input.txt') as file:
    for line in file:
        line = line[:-1]
        print(line, end=' ')
        while True:
            minValue = -1
            substrings = [line.find(digit) for digit in writtenOut]
            for i in range(len(substrings)):
                if substrings[i] > -1:
                    minValue = i
                    break
            if minValue == -1:
                break
            for i in range(minValue+1, len(substrings)):
                if substrings[i] > -1 and (substrings[i] < substrings[minValue] or substrings[minValue] == -1):
                    minValue = i
            line = line.replace(writtenOut[minValue], replacer[minValue])
            # print(' =>', line, end=' ')
        first = 0
        second = 0
        for i in range(len(line)):
            if line[i].isnumeric():
                first = line[i]
                break
        for i in range(len(line)-1, -1, -1):
            if line[i].isnumeric():
                second = line[i]
                break
        value = first + second
        values.append(int(value))
        print(' =>', value)
    print(reduce(lambda a, b: a + b, values))