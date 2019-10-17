import matplotlib.pyplot as plt
from ex5.matrix import GenerateMatrix
from ex5.exercice_1 import find_point as version_naive
from ex5.exercice_2 import find_point as version_better
import time

nb_tests = 10000


def time_for_naive(matrix):
    start = time.time()
    version_naive(matrix)
    return time.time() - start

def time_for_better(matrix):
    start = time.time()
    version_better(matrix)
    return time.time() - start


x = [10, 100, 1000]
y_naive = [0, 0, 0]
y_better = [0, 0, 0]
for nb_test in range(nb_tests):

    matrice = GenerateMatrix().matrix10()
    y_naive[0] += time_for_naive(matrice)
    y_better[0] += time_for_better(matrice)

    matrice = GenerateMatrix().matrix100()
    y_naive[1] += time_for_naive(matrice)
    y_better[1] += time_for_better(matrice)

    matrice = GenerateMatrix().matrix1000()
    y_naive[2] += time_for_naive(matrice)
    y_better[2] += time_for_better(matrice)

for i in range(len(y_naive)):
    y_naive[i] /= nb_tests
    y_better[i] /= nb_tests


plt.plot(x, y_naive, label="Version naive")
plt.plot(x, y_better, label="Version améliorée")
plt.xlabel('Taille de la matrice')
plt.ylabel('Temps d\'éxécution')
plt.title('Test de performance de recherche dans une matrice')
plt.legend()
plt.show()
