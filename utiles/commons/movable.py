import sys
sys.path.insert(0, '.')

from  absMovable import AbstractMovable
from thing import Thing


class Movable(Thing, AbstractMovable):
    def __init__(self, x:int, y:int, literal_name):
        Thing.__init__(self, x, y, literal_name)
        AbstractMovable.__init__(self)

    
if __name__ == '__main__':
    obj = Movable(4, 4, "Thing")
    print(obj)
    obj.move_up()
    print(obj)
    obj.move_down()
    print(obj)
    obj.move_left()
    print(obj)
    obj.move_right()
    print(obj)
    obj.move_right()
    print(obj)
    obj.move_right()
    print(obj)

        

