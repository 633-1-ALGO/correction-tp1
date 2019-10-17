import random


class NumberList:

    def __init__(self):
        # Choisir 15 numéros au hasard entre 0 et 10 
        self.list = random.choices(range(0, 11), k=15)

    def get(self, n):
        return self.list[n]

    def max(self):
        max = -1
        index = -1
        for i in range(len(self.list)):
            if (self.list[i] > max):
                max = self.list[i]
                index = i
        return index

if __name__ == '__main__':
    #Vos tests ici
    pass
