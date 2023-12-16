import sys
sys.path.insert(0, '.')

from utiles.objects.thing import Thing


class Movable(Thing):
    """
    Represents a movable object.

    Attributes:
        x (int): The x-coordinate of the object's position.
        y (int): The y-coordinate of the object's position.
        literal_name (str): The literal name of the object.
        openable (bool): Indicates whether the object is openable or not.
    """

    def __init__(self, x:int, y:int, literal_name):
        Thing.__init__(self, x, y, literal_name)
        self.openable = False
    
    
if __name__ == '__main__':
    obj = Movable(4, 4, "Thing")
    print(obj)

        

