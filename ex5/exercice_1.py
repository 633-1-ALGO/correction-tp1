from ex5.matrix import GenerateMatrix

def find_point(matrix):
    point = [-1, -1]
    for row in range(len(matrix)):
        for column in range(len(matrix[0])):
            if matrix[row][column]:
                point = [row, column]
    return point

if __name__ == '__main__':
    #Vos tests ici
    matrice = GenerateMatrix().random_matrix()
    point = find_point(matrice)

    print(point)
