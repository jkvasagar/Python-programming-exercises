def get_input():
    words = [x for x in input().split(' ')]
    return words


def word_count(words):
    word_list = set(words)
    print(word_list['and'])


if __name__ == '__main__':
    words = get_input()
    word_count(words)
