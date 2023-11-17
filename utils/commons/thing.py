class Thing:
    def __init__(self, literal_name, interactive, collision) -> None:
        self._literal_name = literal_name
        self._interactive = interactive
        self._collision = collision

    @property
    def literal_name(self):
        return self._literal_name

    @literal_name.setter
    def literal_name(self, value):
        self._literal_name = value

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
        return '{}: interactive={}, collision={}'.format(
            self.literal_name, self.interactive, self.collision)

