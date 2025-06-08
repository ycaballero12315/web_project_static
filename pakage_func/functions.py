FILE_PATH = './file/todos.txt'
todos = []

def write_elems(elemts):
    try:
        with open(FILE_PATH, 'w') as ff:
            for elm in elemts:
                ff.writelines(elm.strip() + '\n')
    except FileNotFoundError:
        print('No se encuentra el fichero...')

def read_file():
    try:
        with open(FILE_PATH, 'r') as ff:
            todos = [line.strip() for line in ff if line.strip()]
        return todos

    except FileNotFoundError:
        return []
