import math


if __name__ == '__main__':
    return_list = []
    items = [x for x in input().split(',')]
    for x in items:
        return_list.append(str(int(round(math.sqrt(2*50*float(x)/30)))))
    print(','.join(return_list))
