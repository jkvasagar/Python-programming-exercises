def check(password, funct):
    for letter in password:
        if eval('letter.%s()' % funct):
            return True
    return False


def check_password(password):
    if 6 <= len(password) <= 12:
        if check(password, "islower"):
            if check(password, "isupper"):
                if check(password, "isdigit"):
                    for letter in password:
                        if letter == '#' or letter == '$' or letter == '@':
                            return True
    return False


if __name__ == '__main__':
    passwords = [x for x in input().split(',')]
    for password in passwords:
        if check_password(password):
            print(password),
