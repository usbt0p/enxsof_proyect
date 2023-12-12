import sys
sys.path.insert(0, '.')


from utiles.commons.openable import Openable

class Mixed(Openable):
    def __init__(self, x:int, y:int, literal_name):
        Openable.__init__(self, x, y, literal_name)

if __name__ == '__main__':
    obj = Mixed(4, 4, "Thing")

    print(dir(obj))