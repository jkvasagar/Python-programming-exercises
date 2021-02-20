if __name__ == '__main__':
    values = input()
    numbers = [x for x in values.split(",") if int(x) % 2 != 0]
    print(",".join(numbers))
