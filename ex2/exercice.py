class ArrayList:

    def __init__(self):
        self.list = 'Software Developer An organism that turns caffeine into software'.split(' ')

    def get(self, n):
        return self.list[n]

if __name__ == '__main__':
    liste = ArrayList()
    print(liste.get(3))
