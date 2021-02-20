def square_dict(number: int):
    temp_dict = {}
    for count in range(number):
        temp_dict[count + 1] = (count + 1) * (count + 1)
    return temp_dict


if __name__ == '__main__':
    number = input("Enter a number : ")
    number = int(number)
    print(square_dict(number))
