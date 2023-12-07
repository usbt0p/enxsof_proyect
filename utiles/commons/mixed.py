from  absMovable import AbstractMovable
from openers import Opener


class Mixed(Opener, AbstractMovable):
    def __init__(self, x:int, y:int, literal_name):
        Opener.__init__(self, x, y, literal_name)
        AbstractMovable.__init__(self)

if __name__ == '__main__':
    obj = Mixed(4, 4, "Thing")
    
    print(dir(obj))