from ex5.matrix import GenerateMatrix


def find_point(matrix):
    for row in range(len(matrix)):
        for column in range(len(matrix[0])):
            if matrix[row][column]:
                return [row, column]
    return [-1, -1]

if __name__ == '__main__':
    #Vos tests ici
    matrice = GenerateMatrix().random_matrix()
    point = find_point(matrice)

    print(point)
