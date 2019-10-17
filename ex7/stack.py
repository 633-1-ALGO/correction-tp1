class Stack:

    def __init__(self):
        self._array = []

    def push(self, element):
        self._array.append(element)

    def pop(self):
        return self._array.pop()

    def is_empty(self):
        return len(self._array) == 0

    def empty(self):
        self._array = []
