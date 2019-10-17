import matplotlib.pyplot as plt
from ex4.exercice import equation
import time


nb_tests = 10000
n_tests = [10, 100, 1000]
x = []
y = []

for n in n_tests:

    total_temps = 0
    for nb_test in range(nb_tests):
        start = time.time()
        equation(0, 0, 0, n)
        temps = time.time() - start
        total_temps += temps
    y.append(total_temps / nb_tests)



plt.plot(n_tests, y)
plt.xlabel('Valeurs du n max dans la fonction')
plt.ylabel('Temps d\'éxécution')
plt.title('Test de performance de la fonction equation')
plt.show()
