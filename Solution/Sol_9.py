def get_input():
    line = []
    while True:
        s = input()
        if s:
            line.append(s)
        else:
            break
    return line


def change_upper(lines):
    return_lines = []
    for line in lines:
        return_lines.append(line.upper())
    return return_lines


if __name__ == '__main__':
    list = get_input()
    print('\n'.join(change_upper(list)))
