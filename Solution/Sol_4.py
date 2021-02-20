def get_input():
    x = input("Enter the list of numbers :")
    fList = x.split(',')
    fTuple = tuple(fList)
    print(fList)
    print(fTuple)


if __name__ == '__main__':
    get_input()
