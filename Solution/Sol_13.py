def count_alphanum(line):
    letters = 0
    numbers = 0
    line.lower()
    for letter in line:
        if ord('z') >= ord(letter) >= ord('a'):
            letters += 1
        if ord('9') >= ord(letter) >= ord('0'):
            numbers += 1
    return letters, numbers


if __name__ == '__main__':
    line = input("Enter the string : ")
    letters, numbers = count_alphanum(line)
    print("Letters = ", letters)
    print("Numbers = ", numbers)
