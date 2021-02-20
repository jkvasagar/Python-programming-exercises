def factorial(number: int):
    if number == 0:
        return 1
    if number == 1:
        return 1
    return number * factorial(number - 1)


if __name__ == '__main__':
    number = input("Enter the number you want to find factorial : ")
    number = int(number)
    print ("The output is : ", factorial(number))
