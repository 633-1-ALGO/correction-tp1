from ex7.file_analyser import FileAnalyser

DOSSIER = 'fichiers'

def print_log(correct, incorrect):
    print('Voici les fichiers qui contiennent des erreurs :')
    while not incorrect.is_empty():
        file = incorrect.pop()
        print(file[:file.rfind('.')])
    print('\nVoici les fichiers qui sont corrects :')
    while not correct.is_empty():
        file = correct.pop()
        print(file[:file.rfind('.')])

file_analyser = FileAnalyser()
results = file_analyser.analyse_all_files(DOSSIER)
print_log(results['correct'], results['incorrect'])
