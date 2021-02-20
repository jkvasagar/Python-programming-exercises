from operator import itemgetter


if __name__ == '__main__':
    people = []
    while True:
        person = input()
        if person:
            people.append(person)
        else:
            break
    print(sorted(people,key=itemgetter(0, 1, 2)))
