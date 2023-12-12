import sys
sys.path.insert(0, '.')

class Thing:
    """
    Represents a Thing object with coordinates, a literal name, and collision status.
    """

    def __init__(self, x:int, y:int, literal_name, collision=True):
        """
        Initializes a Thing object.

        Args:
            x (int): The x-coordinate of the Thing.
            y (int): The y-coordinate of the Thing.
            literal_name: The literal name of the Thing.
            collision (bool, optional): Indicates if the Thing can collide with other objects. Defaults to True.
        """
        self.x = x
        self.y = y
        self._literal_name = literal_name
        self._collision = True # FIXME esto por ahora está hardcodeado, pero igual hay q cambiarlo

    @property
    def literal_name(self):
        """
        Returns the literal name of the object.
        """
        return self._literal_name

    @literal_name.setter
    def literal_name(self, value):
        """
        Set the literal name of the object.

        Args:
            value (str): The literal name to set.

        Returns:
            None
        """
        self._literal_name = value

    @property
    def collision(self):
        """Get the collision status of the thing."""
        return self._collision

    @collision.setter
    def collision(self, value):
        """Set the collision value of the thing."""
        self._collision = value
    

    def __str__(self) -> str:
        """
        Returns a string representation of the object.
        
        The string includes the literal name, coordinates (x, y), and collision status.
        
        Returns:
            str: The string representation of the object.
        """
        return '{}: coords=({}, {}), collision={}'.format(
            self.literal_name, self.x, self.y, self.collision)
    

if __name__ == '__main__':
    obj = Thing(1, 2, "Thing")
    asdf = Thing(1, 2, "Thing", False)
    print(asdf)


