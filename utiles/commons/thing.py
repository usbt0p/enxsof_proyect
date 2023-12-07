import sys
sys.path.insert(0, '.')

class Thing:
    def __init__(self, x:int, y:int, literal_name, collision=True):
        self.x = x
        self.y = y
        self._literal_name = literal_name
        self._collision = True # FIXME esto por ahora está hardcodeado, pero igual hay q cambiarlo

    @property
    def literal_name(self):
        return self._literal_name

    @literal_name.setter
    def literal_name(self, value):
        self._literal_name = value

    @property
    def collision(self):
        return self._collision

    @collision.setter
    def collision(self, value):
        self._collision = value
    

    def __str__(self) -> str:
        return '{}: coords=({}, {}), collision={}'.format(
            self.literal_name, self.x, self.y, self.collision)
    

if __name__ == '__main__':
    obj = Thing(1, 2, "Thing")
    asdf = Thing(1, 2, "Thing", False)
    print(asdf)
    print(id(obj))
    print(id(asdf))

