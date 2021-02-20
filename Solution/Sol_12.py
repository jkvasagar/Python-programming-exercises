def check_digit(number: int):
    while number/10 > 0:
        if number % 2 != 0:
            return False
        number = int(number/10)
    return True


def check_digit_over_range(start, end):
    numbers = []
    if start % 2 != 0:
        start = start+1
    for i in range(start, end+1, 2):
        if check_digit(i):
            numbers.append(str(i))
    return numbers


if __name__ == '__main__':
    start = input("Enter start number : ")
    end = input("Enter end number : ")
    start = int(start)
    end = int(end)
    print(','.join(check_digit_over_range(start, end)))
