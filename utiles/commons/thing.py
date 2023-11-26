import sys
sys.path.insert(0, '.')

class Thing:
    def __init__(self, x:int, y:int, literal_name, interactive:bool, collision:bool, movable:bool):
        self.x = x
        self.y = y
        self._literal_name = literal_name
        self._interactive = interactive
        self._collision = collision
        self._movable = movable

    @property
    def literal_name(self):
        return self._literal_name

    @literal_name.setter
    def literal_name(self, value):
        self._literal_name = value

    @property
    def movable(self):
        return self._movable

    @movable.setter
    def movable(self, value):
        self._movable = value

    @property
    def interactive(self):
        return self._interactive

    @interactive.setter
    def interactive(self, value):
        self._interactive = value

    @property
    def collision(self):
        return self._collision

    @collision.setter
    def collision(self, value):
        self._collision = value

    

    def __str__(self) -> str:
        return '{}: coords=({}, {}), interactive={}, collision={}, movable={}'.format(
            self.literal_name, self.x, self.y, self.interactive, self.collision, self.movable)


