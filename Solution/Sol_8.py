def sort(words: list):
    words.sort()
    return words


if __name__ == '__main__':
    words = [x for x in input().split(',')]
    print(','.join(sort(words)))
