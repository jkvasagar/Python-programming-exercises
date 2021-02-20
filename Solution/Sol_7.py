def generate_matrix(x:int, y:int):
    matrix = []
    for x_int in range(x):
        row = []
        for y_int in range(y):
            row.append(x_int*y_int)
        matrix.append(row)
    return matrix


if __name__ == '__main__':
    x = input("Enter x: ")
    y = input("Enter y: ")
    x = int(x)
    y = int(y)
    print(generate_matrix(x,y))
