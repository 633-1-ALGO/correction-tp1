import os


class Loader:

    def load(self, filename):
        my_file = open(filename, 'r')
        return my_file.read()

    def list_folder(self, folder):
        return sorted(os.listdir(folder))
