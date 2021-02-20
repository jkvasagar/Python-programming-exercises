class AddNumber:
    def __init__(self, number: int):
        self.sum_of_numbers = 0
        if number < 7:
            self.sum_of_numbers = 0
        else:
            for i in range(7, number+1, 7):
                self.sum_of_numbers += i


if __name__ == '__main__':
    number = input("Enter the limit : ")
    x = AddNumber(int(number))
    print(x.sum_of_numbers)
