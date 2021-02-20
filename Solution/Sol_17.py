def get_input():
    line = []
    while True:
        s = input()
        if s:
            line.append(s)
        else:
            break
    return line


def calculate_total(lines):
    transaction = {
        'D': [],
        'W': []
    }
    for line in lines:
        words = line.split(' ')
        transaction[words[0]].append(int(words[1]))
    D = sum(transaction['D'])
    W = sum(transaction['W'])
    return D - W


if __name__ == '__main__':
    line = get_input()
    print(calculate_total(line))