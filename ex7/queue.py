class Queue:

    def __init__(self):
        self._array = []

    def push(self, element):
        self._array.append(element)

    def pop(self):
        return self._array.pop(0)

    def is_empty(self):
        return len(self._array) == 0
