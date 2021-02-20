def get_input():
    return [x for x in input().split(' ')]


def count_words (words: list):
    return [word for word in sorted(set(words))]


if __name__ == '__main__':
    print(count_words(get_input()))
