class CharsStorage:

    def __init__(self):
        self._opening = ['(', '{', '[']
        self._closing = [')', '}', ']']

    def __add__(self, opening, closing):
        self._opening.append(opening)
        self._closing.append(closing)

    def is_opening(self, element):
        return element in self._opening

    def is_closing(self, element):
        return element in self._closing

    def is_corresponding_element(self, opening, closing):
        return self._opening.index(opening) == self._closing.index(closing)
