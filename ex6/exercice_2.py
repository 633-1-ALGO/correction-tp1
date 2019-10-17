import math

def power(a, n):
    if n == 0:
        return 1
    if n == 1:
        return a
    if not math.log(n, 2):
        print('Votre n n\est pas un pouvoir de 2!')
        return

    iterations = int(math.log(n, 2))
    for i in range (iterations):
        a = a * a

    return a

if __name__ == '__main__':
    #Vos tests ici
    pass
