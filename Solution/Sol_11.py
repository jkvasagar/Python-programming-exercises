def get_input():
    return [int(number) for number in input().split(',')]


def check_divisible(numbers):
    return_list = []
    for number in numbers:
        if number/5 >= 200 and number % 5 == 0:
            return_list.append(str(number))
    return return_list


if __name__ == '__main__':
    numbers = get_input()
    nums = check_divisible(numbers)
    print(",".join(nums))


