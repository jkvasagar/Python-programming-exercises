import math


def direction(path):
    way = {
        'UP': 0,
        'DOWN': 0,
        'LEFT': 0,
        'RIGHT': 0
    }
    for line in path:
        word = line.split(' ')
        way[word[0]] += int(word[1])
    return way['UP'] - way['DOWN'], way['RIGHT'] - way['LEFT']


if __name__ == '__main__':
    path = []
    while True:
        s = input()
        if s:
            path.append(s)
        else:
            break
    x, y = direction(path)
    print(int(math.sqrt((x*x)+(y*y))))

