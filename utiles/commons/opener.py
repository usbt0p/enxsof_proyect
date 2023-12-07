import sys
sys.path.insert(0, '.')

from utiles.commons.thing import Thing


class Opener(Thing):
    def __init__(self, x:int, y:int, literal_name):
        Thing.__init__(self, x, y, literal_name)
        self.is_open = False

    @property    
    def isOpen(self):
        return self.is_open
    
    def open(self):
        self.is_open = True

    def close(self):
        self.is_open = False

    def __str__(self):
        base_str = super().__str__()  # Call the parent class's __str__ method
        return '{}, open={}'.format(base_str, self.is_open)


if __name__ == '__main__':
    obj = Opener(4, 4, "Thing")
    print(obj)
    obj.open()
    print(obj)
    obj.close()
    print(obj)
