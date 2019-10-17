import random


class GenerateMatrix:
    def __generate_matrix(self, n=None, m=None):
        if n is None:
            n = random.randint(1, 100)
        if m is None:
            m = random.randint(1, 100)

        matrix = [[False for column in range(m)] for row in range(n)]

        n = random.randint(0, n - 1)
        m = random.randint(0, m - 1)

        matrix[n][m] = True

        return matrix

    def random_matrix(self):
        return self.__generate_matrix()

    def matrix10(self):
        return self.__generate_matrix(10, 10)

    def matrix100(self):
        return self.__generate_matrix(100, 100)

    def matrix1000(self):
        return self.__generate_matrix(1000, 1000)
