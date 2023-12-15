import sys
sys.path.insert(0, '.')

from utiles.commons.thing import Thing


class Openable(Thing):
    def __init__(self, x:int, y:int, literal_name):
        """
        Initialize an Openable object.

        Args:
        - x (int): The x-coordinate of the Openable object.
        - y (int): The y-coordinate of the Openable object.
        - literal_name: The literal name of the Openable object.
        """
        Thing.__init__(self, x, y, literal_name)
        self.is_open = False
        self.movable = False

    @property    
    def isOpen(self):
        """
        Check if the Openable object is open.

        Returns:
        - bool: True if the Openable object is open, False otherwise.
        """
        return self.is_open
    
    def open(self):
        """
        Open the Openable object.
        """
        self.is_open = True

    def close(self):
        """
        Close the Openable object.
        """
        self.is_open = False

    def __str__(self):
        """
        Return a string representation of the Openable object.

        Returns:
        - str: A string representation of the Openable object.
        """
        base_str = super().__str__()  # Call the parent class's __str__ method
        return '{}, open={}'.format(base_str, self.is_open)


if __name__ == '__main__':
    obj = Openable(4, 4, "Thing")
    print(obj)
    obj.open()
    print(obj)
    obj.close()
    print(obj)
    print(obj.isOpen)
