def count_case(line):
    upper = 0
    lower = 0
    for letter in line:
        if letter.isupper():
            upper += 1
        elif letter.islower():
            lower += 1
    return upper, lower


if __name__ == '__main__':
    line = input('Enter the sentence : ')
    upper,lower = count_case(line)
    print("Upper : ", upper)
    print("Lower : ", lower)
