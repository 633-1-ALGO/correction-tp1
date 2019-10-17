from ex7.stack import Stack
from ex7.queue import Queue
from ex7.loader import Loader
from ex7.charsstorage import CharsStorage


class FileAnalyser:

    def __init__(self):
        self._loader = Loader()
        self._pile = Stack()
        self._correct = Queue()
        self._incorrect = Queue()
        self._chars = CharsStorage()

    def _analyse_single_file(self, file):
        self._pile.empty()
        for char in file:
            if self._chars.is_opening(char):
                self._pile.push(char)
            elif self._chars.is_closing(char):
                c = self._pile.pop()
                if not self._chars.is_corresponding_element(c, char):
                    raise Exception()
        if not self._pile.is_empty():
            raise Exception()

    def analyse_all_files(self, folder):
        files = self._loader.list_folder(folder)
        for filename in files:
            file_source = self._loader.load(folder + '\\' + filename)
            try:
                self._analyse_single_file(file_source)
                self._correct.push(filename)
            except Exception:
                self._incorrect.push(filename)

        return {'correct': self._correct, 'incorrect': self._incorrect}
