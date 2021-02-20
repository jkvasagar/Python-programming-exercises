def find_number(start: int, end: int):
    answer = []
    for number in range(start, end+1):
        if number % 7 == 0:
            if number % 5 != 0:
                answer.append(number)
    for i in range(len(answer) - 1):
        print(answer[i], end=',')
    print(answer[-1])


if __name__ == '__main__':
    find_number(2000, 3200)
